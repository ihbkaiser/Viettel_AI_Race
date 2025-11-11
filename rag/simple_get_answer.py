from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed
from datasets import Dataset
import pandas as pd
import json
import random
from tqdm import tqdm
# Configuration
DEFAULT_MODEL = "gpt-4o-mini"
SERVER_HOST = "https://openrouter.ai/api"
TEMPERATURE = 0.0
TOP_P = 0.9
MAX_TOKENS = 2048
DATA_AND_SUMMARY_PATH = "data/processed/summary/private_test_data_summary.json"
API_KEY = None
QUESTION_PATH = "data/processed/private_question/question.csv"
ANSWER_PATH = "data/processed/private_answer/answer.json"


def get_completion_vllm(
    input_prompt,
    system_prompt=None,
    model=DEFAULT_MODEL,
    temperature=TEMPERATURE,
    top_p=TOP_P,
    max_tokens=MAX_TOKENS,
    server_host=SERVER_HOST,
    api_key=API_KEY,
):
    client = OpenAI(
        api_key=api_key,
        base_url=f"{server_host}/v1",
    )
    messages = []
    if system_prompt is not None:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": input_prompt})
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            seed=0,
            top_p=top_p,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return None

def multi_thread_task_dict(task_dictionary, num_workers=1, show_progress=True):
    final_results = {}
    futures = []

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for id_, task in task_dictionary.items():
            futures.append(
                executor.submit(
                    lambda id_=id_, task=task: {"id": id_, "task_result": task()}
                )
            )

        if show_progress:
            with tqdm(total=len(futures)) as pbar:
                for future in as_completed(futures):
                    result = future.result()
                    final_results[result["id"]] = result["task_result"]
                    pbar.update(1)
        else:
            for future in as_completed(futures):
                result = future.result()
                final_results[result["id"]] = result["task_result"]

    return final_results

def parse_json(json_text):
    first = json_text.find("{")
    last = json_text.rfind("}")
    return json.loads(json_text[first:last+1])


def word_count(text):
    return len(text.split())


AUGMENT_QUESTION_PROMPT = """
You will be given a question that need to search for information before answer. Your job is to generate {{k}} different Vietnamese queries to find information for the question.
The queries should be diverse and different from each other.
Return only the augmented queries without other information. Each query in one line.

### Question: {{question}}
""".strip()

DOCUMENT_RETRIEVAL_PROMPT = """
You will be given a list of document summary and a list of queries. Try to return the top up to {{top_documents}} documents that best match with the queries.
The document summary will be given along with the index of that document (e.g., "index, summary_content"). Return only the index of the best match documents in the json format without other information: {"document_indices": [1,3,4,...]}. If you can not find relevant documents for the queries, simply return {"document_indices": null}.
### Document Summaries
{{document_summaries}}

### Queries
{{queries}}
""".strip()

QUESTION_ANSWERING_PROMPT = """
Please answer the multiple choice question grounding on the given context.
The question is a multiple choice question with 4 options (A, B, C, D) and there can be multiple correct answers.
Return the answer in the following json format: {"answers": ["A", "B", "C", "D"]} or {"answers": []} if you can not find the answer in the context.

### Question
{{question}}

### Context
{{context}}
""".strip()


def get_augmented_queries(question, num_queries=5):
    question_text = f"""{question['Question']}\n{question['A']}\n{question['B']}\n{question['C']}\n{question['D']}"""
    prompt = AUGMENT_QUESTION_PROMPT.replace("{{question}}", question_text).replace("{{k}}", str(num_queries))
    output = get_completion_vllm(prompt)
    return [x.strip() for x in output.split("\n") if x]


def split_summary_and_convert_to_index(chunks, max_chunk_words=1024):
    summary_chunks = []
    total_words = 0
    for i, chunk in enumerate(chunks):
        num_words = word_count(chunk)
        if len(summary_chunks) == 0 or (total_words + num_words > max_chunk_words):
            summary_chunks.append([(i, chunk)])
            total_words = num_words
        else:
            summary_chunks[-1].append((i, chunk))
            total_words += num_words
    return summary_chunks


def get_relevant_document_indices(augmented_queries, summary_chunk, top_documents=3):
    document_summaries = "\n".join([f"{i}, {content}" for i, content in summary_chunk])
    augmented_queries_text = "\n".join(augmented_queries)
    prompt = DOCUMENT_RETRIEVAL_PROMPT.replace("{{document_summaries}}", document_summaries).replace("{{queries}}", augmented_queries_text).replace("{{top_documents}}", str(top_documents))
    output = get_completion_vllm(prompt)
    output = parse_json(output)
    return output["document_indices"]


def answer_question_with_context(question, context):
    input_question = question['Question'] + "\n" + "\n".join([question['A'], question['B'], question['C'], question['D']])
    prompt = QUESTION_ANSWERING_PROMPT.replace("{{question}}", input_question).replace("{{context}}", context)
    output = get_completion_vllm(prompt)
    try:
        return parse_json(output)["answers"]
    except:
        return None


def get_final_answer(question, data_and_summary, log_progress=False):
    augmented_queries = get_augmented_queries(question)
    document_summaries = [x["document_summary"] for x in data_and_summary]
    summaries_combined = split_summary_and_convert_to_index(document_summaries)
    document_indices = []
    for summary_chunk in tqdm(summaries_combined, disable=not log_progress):
        selected_indices = get_relevant_document_indices(augmented_queries, summary_chunk)
        if selected_indices:
            document_indices.extend(selected_indices)    
    selected_documents = [data_and_summary[i] for i in document_indices]
    all_answers = []
    for document in tqdm(selected_documents, disable=not log_progress):
        for chunk in document['chunks']:
            answer = answer_question_with_context(question, chunk['chunk_content'])
            if answer:
                all_answers.extend(answer)
    is_random = False
    if all_answers:
        final_answers = list(set(all_answers))
    else:
        is_random = True
        final_answers = [random.choice(["A", "B", "C", "D"])]
    return {
        "answers": final_answers,
        "is_random": is_random
    }


def load_data_and_summary(data_path=DATA_AND_SUMMARY_PATH):
    with open(data_path) as f:
        return json.load(f)

def get_answer_task(question, data_and_summary, log_progress=False):
    answer = get_final_answer(question, data_and_summary, log_progress=log_progress)
    print("Question: ", question)
    print("Answer: ", answer)
    question['answers'] = answer['answers']
    question['is_random'] = answer['is_random']
    return question

if __name__ == "__main__":
    questions = Dataset.from_pandas(pd.read_csv(QUESTION_PATH))
    data_and_summary = load_data_and_summary()
    task_dict = {
        i: lambda question=question, data_and_summary=data_and_summary: get_answer_task(question, data_and_summary)
        for i, question in enumerate(questions)
    }
    task_results = multi_thread_task_dict(task_dict, num_workers=10)
    with open(ANSWER_PATH, "w") as f:
        json.dump(list(task_results.values()), f, ensure_ascii=False)

