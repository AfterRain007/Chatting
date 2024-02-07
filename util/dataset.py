import json
from datetime import datetime
import pandas as pd

def readFile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # To Take which date format your data has.
    ## If you live in a sane country don't worry this won't take long
    ### Unless you have year in the middle as a format, shame on you
    date_format_list = ["%d/%m/%Y %H:%M", "%m/%d/%Y %H:%M", "%Y/%d/%m %H:%M",
                        "%Y/%m/%d %H:%M", "%d/%Y/%m %H:%M", "%m/%Y/%d %H:%M"]

    for x in date_format_list:
      for line in lines[:5]:
        try:
          parts = line.split(' - ')
          date_str, time_str = parts[0].split(', ')
          (datetime.strptime(date_str + " " + time_str, x))
          date_format = x
          break
        except:
          continue
          
    # Extract data from each line and create a list
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