import json
from datetime import datetime
import pandas as pd

def readFile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract data from each line and create a list of tuples
    date_format = "%d/%m/%Y %H:%M"
    data = []
    for line in lines:
        try:
            parts = line.split(' - ')
            date_str, time_str = parts[0].split(', ')
            sender, message = parts[1].split(': ', 1)
            data.append((datetime.strptime(date_str + " " + time_str, date_format), sender, message[:-1]))
        except:
            continue

    df = pd.DataFrame(data)
    df.rename(columns={0:"date", 1: "name", 2: 'text'}, inplace = True)
    df.set_index('date', inplace = True)
    
    return df

def readBadWord(lan):
    with open(('./data/badWords.json'), encoding="utf-8") as f:
        badWords = json.load(f)

    filtered_list = [item['word'] for item in badWords['RECORDS'] if item['language'] == lan]
    f.close()
    return filtered_list