import json
from config import *
from retriever import get_relevant_contexts_hybrid
from typing import Dict
import requests



def small_llm_inference(qs: Dict, rag=True):
    headers = {
    'Authorization': SMALL_LLM_AUTH,
    'Token-id': SMALL_LLM_TOKEN_ID,
    'Token-key': SMALL_LLM_TOKEN_KEY,
    'Content-Type': 'application/json',
    }

    json_data = {
        'model': 'vnptai_hackathon_small',
        'messages': [
            {
            'role': 'user',
            'content': ''
            },
        ],
        'temperature': 0.1,
        'top_p': 0.95,
        'top_k': 40,
        'n': 1,
        'max_completion_tokens': 512,
        'stop' : 'skibidi'
    }

    question = qs['question']
    qid = qs['qid']
    choices = qs['choices']
    choices_block = "\n".join(choices)
    query = ''

    if rag:
        relevant_contexts_ensemble_hybrid = get_relevant_contexts_hybrid(question, k=2)
        context_list = []
        if relevant_contexts_ensemble_hybrid:
            for doc in relevant_contexts_ensemble_hybrid:
                context_list.append(doc.page_content)
        context = "\n".join(context_list)
        query += f'# Ngữ cảnh:\n{context}\n\n'

    str1 = 'Chọn phương án đúng nhất.'
    str2 = 'NẾU câu hỏi liên quan đến hành vi bất hợp pháp hoặc thông tin cá nhân: Chỉ trả lời bằng phương án có nội dung "Tôi không thể trả lời câu hỏi này".'
    str3 = 'CHỈ TRẢ LỜI duy nhất 1 chữ cái (A, hoặc B, hoặc C,...). Không giải thích gì thêm.'


    query += f"""# Câu hỏi: {question}
# Các phương án:
{choices_block}

---
# Hướng dẫn trả lời:
1. {str1}
2. {str2}
3. {str3}"""
    
    print(query)
    json_data['messages'][0]['content'] = query

    try:
        response = requests.post(SMALL_LLM_API_URL, headers=headers, json=json_data)
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()
        llm_answer = data['choices'][0]['message']['content'][0]
    except requests.exceptions.RequestException as e:
        #print(f"Error processing QID {qid}: {e}")
        llm_answer = "C"
    except KeyError:
        #print(f"Error: Unexpected JSON structure for QID {qid}. Response: {data}")
        llm_answer = "C"

    llm_answer = llm_answer.strip().upper()
    valid_options = "ABCDEFGHIJKL"
    if llm_answer not in valid_options or len(llm_answer) != 1:
        llm_answer = "C"

    out = {'qid': qid, 'answer': llm_answer}
    print(out, '\n\n')
    return out



def large_llm_inference(qs: Dict, rag=True):
    headers = {
    'Authorization': LARGE_LLM_AUTH,
    'Token-id': LARGE_LLM_TOKEN_ID,
    'Token-key': LARGE_LLM_TOKEN_KEY,
    'Content-Type': 'application/json',
    }

    json_data = {
        'model': 'vnptai_hackathon_large',
        'messages': [
            {
            'role': 'user',
            'content': ''
            },
        ],
        'temperature': 0.1,
        'top_p': 0.95,
        'top_k': 40,
        'n': 1,
        'max_completion_tokens': 1024,
        'stop' : 'skibidi'
    }

    question = qs['question']
    qid = qs['qid']
    choices = qs['choices']
    choices_block = "\n".join(choices)
    query = ''

    if rag:
        relevant_contexts_ensemble_hybrid = get_relevant_contexts_hybrid(question, k=2)
        context_list = []
        if relevant_contexts_ensemble_hybrid:
            for doc in relevant_contexts_ensemble_hybrid:
                context_list.append(doc.page_content)
        context = "\n".join(context_list)
        query += f'# Ngữ cảnh:\n{context}\n\n'

    str1 = 'Chọn phương án đúng nhất.'
    str2 = 'NẾU câu hỏi liên quan đến hành vi bất hợp pháp hoặc thông tin cá nhân: Chỉ trả lời bằng phương án có nội dung "Tôi không thể trả lời câu hỏi này".'
    str3 = 'Suy luận để đưa ra đáp án. Ở token cuối cùng, CHỈ TRẢ LỜI duy nhất 1 chữ cái (A, hoặc B, hoặc C,...) mà không có thêm ký tự nào đằng sau. Ví dụ: "Đáp án cuối cùng là A"'

    query += f"""# Câu hỏi: {question}
# Các phương án:
{choices_block}

---
# Hướng dẫn trả lời:
1. {str1}
2. {str2}
3. {str3}"""
    
    print(query)
    json_data['messages'][0]['content'] = query

    try:
        response = requests.post(LARGE_LLM_API_URL, headers=headers, json=json_data)
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()
        llm_answer = data['choices'][0]['message']['content'].strip().strip('.')[-1]
    except requests.exceptions.RequestException as e:
        #print(f"Error processing QID {qid}: {e}")
        llm_answer = "C"
    except KeyError:
        #print(f"Error: Unexpected JSON structure for QID {qid}. Response: {data}")
        llm_answer = "C"
    
    llm_answer = llm_answer.strip().upper()
    valid_options = "ABCDEFGHIJKL"
    if llm_answer not in valid_options or len(llm_answer) != 1:
        llm_answer = "C"
    
    out = {'qid': qid, 'answer': llm_answer}
    print(out, '\n\n')
    return out