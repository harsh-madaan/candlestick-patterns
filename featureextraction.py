import os.path
import glob
import pandas as pd
import candlestick_attributes as ca

def window (data,n):
    windowlist =[]
    for i in range(0,data.shape[0]-n+1):
        elem = []
        for j in range(i,i+n):
            elem.append(data.iloc[j])

        windowlist.append(elem)

    return (windowlist)

def getbasefeatures(data):
    base_features_df = pd.DataFrame(
        columns=['C1Open','C1High','C1Low','C1Close','C1Vol',
                 'C2Open','C2High','C2Low','C2Close','C2Vol',
                 'C3Open','C3High','C3Low','C3Close','C3Vol'])
    base_features_records = []
    for i in range(0, len(data) - 2):
        C1Open = data[i][0]['open']
        C1High = data[i][0]['high']
        C1Low = data[i][0]['low']
        C1Close = data[i][0]['close']
        C1Vol = data[i][0]['volume']

        C2Open = data[i][1]['open']
        C2High = data[i][1]['high']
        C2Low = data[i][1]['low']
        C2Close = data[i][1]['close']
        C2Vol = data[i][1]['volume']

        C3Open = data[i][2]['open']
        C3High = data[i][2]['high']
        C3Low = data[i][2]['low']
        C3Close = data[i][2]['close']
        C3Vol = data[i][2]['volume']

        base_features_record = pd.Series([C1Open,C1High,C1Low,C1Close,C1Vol,C2Open,C2High,C2Low,C2Close,C2Vol,C3Open,C3High,C3Low,C3Close,C3Vol]
                                         ,index = base_features_df.columns)
        base_features_records.append(base_features_record)
    base_features_df = pd.DataFrame(base_features_records)
    return base_features_df

    #print(base_features_df.head())
    #base_features_df.to_csv('C:\\Users\\Harsh\\Documents\\temp.csv')

def getcomplexfeatures(data):
    #print(data.iloc[0])
        for i in range(0, len(data)):
            C1Color = ca.candleColor(data.iloc[i]['C1Open'], data.iloc[i]['C1Close'])
            C2Color = ca.candleColor(data.iloc[i]['C2Open'], data.iloc[i]['C2Close'])
            C3Color = ca.candleColor(data.iloc[i]['C3Open'], data.iloc[i]['C3Close'])

            C1Body = ca.candleBody(data.iloc[i]['C1Open'], data.iloc[i]['C1Close'])
            C2Body = ca.candleBody(data.iloc[i]['C2Open'], data.iloc[i]['C2Close'])
            C3Body = ca.candleBody(data.iloc[i]['C3Open'], data.iloc[i]['C3Close'])

            C1UWick = ca.candleUpperWick(data.iloc[i]['C1Open'], data.iloc[i]['C1Close'],data.iloc[i]['C1High'])
            C2UWick = ca.candleUpperWick(data.iloc[i]['C2Open'], data.iloc[i]['C2Close'], data.iloc[i]['C2High'])
            C3UWick = ca.candleUpperWick(data.iloc[i]['C3Open'], data.iloc[i]['C3Close'], data.iloc[i]['C3High'])










data = pd.read_csv('C:\\Users\\Harsh\\Documents\\BANKNIFTY_F15.csv')
base_features_df = getbasefeatures(window(data,3))
getcomplexfeatures(base_features_df)