import plotly.graph_objects as go
from os import listdir
import os.path

import glob
import pandas as pd
import patterns as patterns



#print(df.head(10))


def plotcandles(df,n,pattern):
    global imagenum
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])],
                    layout={

                        'template': "simple_white",
                        'xaxis_rangeslider_visible': False,
                        'showlegend': False,
                        'hovermode': 'x',
                        'xaxis': {
                            # 'rangebreaks': [
                            #     dict(bounds=["sat", "mon"]),  # hide weekends
                            #
                            # ],
                            'type' : 'category',
                            'showgrid' : False,
                            'visible' : False,
                        },
                        'yaxis': {
                            # 'rangebreaks': [
                            #     dict(bounds=["sat", "mon"]),  # hide weekends
                            #
                            # ],

                            'showgrid': False,
                            'visible': False,
                        },
                    },
                    )
    #fig.show()
    imageroot = "C:\\Users\\Harsh\\Documents\\Kite Data\\Images\\%s\\" % pattern
    imagepath = "C:\\Users\\Harsh\\Documents\\Kite Data\\Images\\%s\\fig%s.png" % (pattern,imagenum)

    if(pattern):
        if not os.path.exists(imageroot):
            os.makedirs(imageroot)
        fig.write_image(imagepath)
        imagenum += 1



def window (data,n):
    windowlist =[]
    for i in range(0,data.shape[0]-n+1):
        elem = []
        for j in range(i,i+n):
            elem.append(data.iloc[j])

        windowlist.append(elem)

    return (windowlist)

def getpics(data):


    for i in range (0,len(data)-2):
        #pattern = 'test'
        #print(data[i])
        candle1 = data[i][0]
        candle2 = data[i][1]
        pattern = ""
        if(patterns.isBullishReversal(candle1,candle2)):
            pattern = 'BullishReversal'
        #if(patterns.isInvHammer(candle)):
            #candle = data[i][0]

            # print('Body - ',abs(candle['open']-candle['close']))
            # print('UWick - ',(candle['high'] - (max(candle['open'],candle['close']))))
            # print('LWick - ',((min(candle['open'],candle['close'])) - candle['close']))
            #

        elif(patterns.isBearishReversal(candle1,candle2)):
            pattern = 'BearishReversal'
        data[i].append(data[i + 1][1])
        data[i].append(data[i + 2][1])
        plotcandles(pd.DataFrame(data[i]), imagenum, pattern)


directory = "C:\\Users\\Harsh\\Documents\\Kite Data\\"
files = list(glob.iglob(directory + '**/**.csv', recursive=True))
imagenum = 0
# for file in files:
#     #print(file)
#     data = pd.read_csv(file)
#     getpics((window(data,2)))

data = pd.read_csv('C:\\Users\\Harsh\\Documents\\BANKNIFTY_F1.csv')
getpics(window(data,2))





