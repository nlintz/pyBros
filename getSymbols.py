file = open('tickers.txt')
def returnStockTickers():
    stock=[]
    for line in file:
        if len(line)>3:
            line=line[0:3]
        preformat = line.split('//')[0].split('\n')[0].split('^')[0]
        line=preformat
        stock.append(line)
    return stock
