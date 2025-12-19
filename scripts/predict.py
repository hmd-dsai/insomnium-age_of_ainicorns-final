from config import JSON_TEST_PATH
from llm_call_config import large_llm_inference, small_llm_inference
import json

with open(JSON_TEST_PATH, 'r') as f:
    test_data = json.load(f)
print("JSON data loaded into 'test_data' variable.")

questions_for_llm_test = []
for item in test_data:
    questions_for_llm_test.append({
        'qid': item['qid'],
        'question': item['question'],
        'choices': [f'{chr(char_code)}. {opt}' for char_code, opt in enumerate(item['choices'], start=65)]
    })

print(f"Extracted {len(questions_for_llm_test)} questions from test_data.")

result = []

for item in questions_for_llm_test:
    if "$" in item['question']:
        result.append(large_llm_inference(item, rag=False))
    elif len(item['choices']) >= 5:
        result.append(large_llm_inference(item, rag=True))
    elif len(item['question']) > 3000:
        result.append(small_llm_inference(item, rag=False))
    else:
        result.append(small_llm_inference(item, rag=True))

import csv

print(result)

fieldnames = ["qid", "answer"]

# Specify the filename
filename = '/code/submission.csv'

# Open the file in write mode
with open(filename, mode="w", newline="") as csvfile:
    # Create a DictWriter object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for row in result:
        writer.writerow(row)