from util.dataset import *
from util.Preprocessing import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    print("\n(See github.com/AfterRain007/Chatting ReadME file for language support!)")
    lan = input("Language of Your Data: ")
    df = readFile('./data/target.txt')
    badWords = readBadWord(lan)
    
    df['bad'] = df['text'].str.contains("|".join(badWords), case=False, regex = True)
    badCounts = df[df['bad']==True].value_counts(['name'])

    df = PreprocessingText(df)
    df = df[['name', 'replyTime']].groupby('name').mean()
    df.rename(columns = {'replyTime':"Average Reply Time"}, inplace = True)
    df.to_csv("./res/resultTime.csv")
    
    plt.bar(badCounts.index.get_level_values(0), badCounts.values)
    plt.tight_layout()
    plt.savefig('./res/resultBad.png')
    print("It's done! Self Destructing in")
    time.sleep(0.5)
    for x in np.arange(3):
        print(3-x)
        time.sleep(1)

if __name__ == "__main__":
    main()
