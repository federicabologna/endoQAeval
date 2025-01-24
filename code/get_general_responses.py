# Imports
import time
import os
import argparse
import csv
import numpy as np
import pandas as pd
import openai
from   sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# send API request to OpenAI's API to receive generated answers to questions
def get_response(system_prompt, _question, model='gpt4', _max_tokens=500):

    attempts = 0
    max_attempts = 3
    response = 'None'

    while attempts < max_attempts:
        try:
            response = openai.ChatCompletion.create(
                engine=model,
                max_tokens=_max_tokens,
                messages = [
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': _question}
                ]
            )
            _answer = response['choices'][0]['message']['content'].strip().lower()
        except Exception as e:
            print(f'Error {e}. Sleeping 3 seconds ...')
            time.sleep(3)
            if attempts == max_attempts-1:
                _answer = f'Error {e}'
        attempts += 1
        if model == 'gpt4':
            time.sleep(2)
        else:
            time.sleep(0.5)

    return _answer


def main():

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--output_folder', required=True, type=str)
    # args = parser.parse_args()
    # output_folder = args.output_folder

    parser = argparse.ArgumentParser()
    parser.add_argument('--start_row', required=True, type=int)
    parser.add_argument('--end_row', required=True, type=int)
    #parser.add_argument('--n_responses', required=True, type=int)
    args = parser.parse_args()
    start_row = args.start_row
    end_row = args.end_row
    #n_responses = args.n_responses

    # File locations
    dir = os.getcwd()
    out_dir = os.path.join(dir, 'output')
    fig_dir = os.path.join(dir, 'figures')
    os.makedirs(fig_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    # API settings
    openai.api_type = 'azure'
    openai.api_version = '2023-05-15'
    openai.api_key = open(os.path.join('../apikeys', 'endoqa-key.txt')).read().strip()
    openai.api_base = 'https://endoqa-cornell.openai.azure.com/'

    # Set prompts
    prompts = {'no_prompt': ''}

    # Output folder for general answers
    output_dir = os.path.join(out_dir, 'general_responses')
    os.makedirs(output_dir, exist_ok=True)

    # Source file with general questions
    questions = pd.read_csv(os.path.join(dir, 'data', 'general_questions.csv'))
    df = questions[start_row:end_row]

    for index, row in df.iterrows(): # for each question

        start = time.time()

        id = row['id']
        question = row['text']

        output_path = os.path.join(output_dir,  f'{id}-responses.csv')

        if not os.path.exists(output_path): # if output file doesn't exist for answer
            with open(output_path, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                row = ['question_id', 'prompt_type', 'response']
                csvwriter.writerow(row)

            for prompt_type, prompt in prompts.items():
                n_tokens = 250
                answer = get_response(prompt, question, _max_tokens=n_tokens) # get answer from GPT-4

                with open(output_path, 'a') as csvfile: # save in CSV file
                    csvwriter = csv.writer(csvfile)
                    row = [id, prompt_type, answer]
                    csvwriter.writerow(row)

        end = time.time()  
        print(id, end-start)


if __name__ == "__main__":
    main()