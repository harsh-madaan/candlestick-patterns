import pandas as pd

def txt2csv (filename,filedest):
    file = pd.read_csv(filename, header = None)
    file.columns = ['filename','date','time','open','high','low','close','volume','etc']
    file.to_csv(filedest,index = None)



file1 = 'C:\\Users\\Harsh\\Documents\\BANKNIFTY_F1.txt'

file2 = 'C:\\Users\\Harsh\\Documents\\BANKNIFTY_F1.csv'

file3 = 'C:\\Users\\Harsh\\Documents\\BANKNIFTY_F15.csv'

#txt2csv(file1,file2)

def onemin_to_fivemin (filename):

    #df = pd.read_csv(filename, parse_dates = [["date", "time"]], index_col=0)
    df = pd.read_csv(filename)
    # print(df.head())
    #df["date"] = pd.to_datetime(df['date'])
    #df.set_index("date", inplace=True)
    df.drop(df[df['time']>'15:30'].index,inplace = True)

    #df.set_index()
    df['date'] = (pd.to_datetime(df['date'], format='%Y%m%d')).dt.strftime('%Y-%m-%d')
    df['time'] = pd.to_datetime(df['time'], format='%H:%M').dt.strftime('%H:%M:%S')
    #print(df.head())
    df['Datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df = df.set_index('Datetime')
    #print(df.head())

    df = df.groupby(pd.Grouper(freq='5T')).agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum"
    })

    #df.drop((df.index.to_series().dt.time).strftime('%H:%M') > '15:30')

    df.to_csv(file3)

#txt2csv(file1,file2)
onemin_to_fivemin(file2)
