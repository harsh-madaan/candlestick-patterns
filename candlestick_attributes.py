def candleColor(open,close):
    return 'Green' if open < close else 'Red'

def candleBody(open,close):
    return abs(open-close)

def candleUpperWick(open,close,high):
    return (high - (max(open,close,)))