#pyJit caller
import py2jit
companies = ['CAG', 'AAPL']
color_dict = {'Industries':'D0D9C8','Financials':'FDBD27','Healthcare':'DA5915','Consumer Discretionary':'4813A4','Utilities':'1581F5','Information Technology':'333333','Materials':'5FFF00','Energy':'808099','Consumer Staples':'003399','Telecom':'CCCCCC'}
py2jit.main(companies, color_dict)
