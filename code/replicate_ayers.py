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
def get_response(_prompt, model='gpt4', _max_tokens=500):

    attempts = 0
    max_attempts = 3
    system__prompt = ''''''  ## for few-shot
    response = 'None'

    while attempts < max_attempts:
        try:
            response = openai.ChatCompletion.create(
                engine=model,
                max_tokens=_max_tokens,
                messages = [
                    #{'role': 'system', 'content': system__prompt},
                    {'role': 'user', 'content': _prompt}
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
    parser.add_argument('--n_responses', required=True, type=int)
    args = parser.parse_args()
    start_row = args.start_row
    end_row = args.end_row
    n_responses = args.n_responses

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
    
    # Source file with general questions
    ayers = pd.read_csv(os.path.join(dir, 'data', 'ayers2023.csv'))

    # Output folder for general answers
    replication_dir = os.path.join(out_dir, 'replication_ayers')
    os.makedirs(replication_dir, exist_ok=True)

    df = ayers[start_row:end_row]

    for index, row in df.iterrows(): # for each question

        start = time.time()

        id = row['postID']
        question = row['Question']

        output_path = os.path.join(replication_dir,  f'replication_ayers_{id}.csv')

        if not os.path.exists(output_path): # if output file doesn't exist for answer
            with open(output_path, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                row = ['question_id', 'response_id', 'response']
                csvwriter.writerow(row)

            for n in range(1,n_responses+1):
                response_id = f'response_{n}'
                print(response_id)
                n_tokens = 250
                answer = get_response(question, _max_tokens=n_tokens) # get answer from GPT-4

                with open(output_path, 'a') as csvfile: # save in CSV file
                    csvwriter = csv.writer(csvfile)
                    row = [id, response_id, answer]
                    csvwriter.writerow(row)

        end = time.time()  
        print(id, end-start)


if __name__ == "__main__":
    main()