from util.dataset import *
from util.Preprocessing import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    print("(See github.com/AfterRain007/Chatting ReadME file for language support!)")
    lan = input("Language of Your Data: ")
    df = readFile('./data/target.txt')
    badWords = readBadWord(lan)
    
    df['bad'] = df['text'].str.contains("|".join(badWords), case=False, regex = True)
    badCounts = df[df['bad']==True].value_counts(['name'])

    df = PreprocessingText(df)
    df = df[['name', 'replyTime']].groupby('name').mean()
    df.to_excel("./res/resultTime.xlsx")
    
    plt.bar(badCounts.index.get_level_values(0), badCounts.values)
    plt.tight_layout()
    plt.savefig('./res/resultBad.png')
    badCounts.to_csv('./res/resultTime.csv')
    print("It's done! Self Destructing in")

    for x in np.arange(5):
        print(5-x)
        time.sleep(1)

if __name__ == "__main__":
    main()
