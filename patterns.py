
def candleBody(candle):
    return abs(candle['open'] - candle['close'])

def candleUpperWick(candle):
    return (candle['high'] - (max(candle['open'],candle['close'])))

def candleLowerWick(candle):
    return ((min(candle['open'],candle['close'])) - candle['low'])

def isGreen(candle):
    return candle['open'] < candle['close']

def isRed(candle):
    return candle['open'] > candle['close']

def isInvHammer(candle):
    return (isRed(candle) and (candleUpperWick(candle) > (candleBody(candle))) and (candleLowerWick(candle) < (candleUpperWick(candle))))

def isHammer(candle):
    return (isGreen(candle) and (candleLowerWick(candle) > (candleBody(candle))) and (candleUpperWick(candle) < candleLowerWick(candle)))

def isBullish(candle):
    return(isGreen(candle) and (candleLowerWick(candle) * 3 < candleBody(candle)) and (candleUpperWick(candle) * 4 < candleBody(candle)))

def isBearish(candle):
    return(isRed(candle) and (candleLowerWick(candle) * 3 < candleBody(candle)) and (candleUpperWick(candle) * 4 < candleBody(candle)))

def isGapUp(candle1,candle2):
    return(candle1['close']<candle2['open'])


def isGapDown(candle1,candle2):
    return(candle1['close']>candle2['open'])


def isBearishReversal(candle1,candle2):
    return(isBullish(candle1) and isInvHammer(candle2))

def isBullishReversal(candle1,candle2):
    return(isBearish(candle1) and isHammer(candle2))



