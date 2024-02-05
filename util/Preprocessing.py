import pandas as pd
import datetime as datetime
import numpy as np

def PreprocessingText(df):
    df.loc[:, 'replyTime'] = df.index.diff()
    df.loc[:, 'day'] = df.index.day
    
    df = df[df['replyTime'] < '12:00:00']
    
    maskN = []
    maskD = []
    for x in np.arange(len(df)):
        if df.iloc[x-1]['name'] == df.iloc[x]['name']:
            maskN.append(x)
    maskN = maskN[1:]
    dfMasked = df.reset_index().drop(maskN)
    dfMasked.reset_index(drop = True, inplace = True)
    
    for x in np.arange(len(dfMasked)):
        if dfMasked.iloc[x-1]['day'] != dfMasked.iloc[x]['day']:
            maskD.append(x)
    maskD = maskD[1:]
    dfMasked = dfMasked.drop(maskD)
    
    return dfMasked