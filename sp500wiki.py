import urllib2
from bs4 import BeautifulSoup as bs
from HTMLParser import HTMLParser
import csv

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'pyBros')]
response = opener.open("http://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
page = response.read()

bsoup = bs(page, "lxml")
companies = bsoup.find("table", {"class":"wikitable"})

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

records = []
indices = []
comps = companies.find_all('tr')

th_html = str(comps[0])
header = strip_tags(th_html).strip('\n').split('\n')
indices.append(header.index('SEC filings'))
indices.append(header.index('Address of Headquarters'))
indices[-1] = indices[-1]-1

for comp in comps:
	html = str(comp)
	row = strip_tags(html).strip('\n').split('\n')
	for index in indices:
		del row[index]
	records.append(row)

def createCSV(companies, header = False):
	if not header:
		del companies[0]
	myFile = open('sp500.csv','wb')
	wr = csv.writer(myFile, quoting = csv.QUOTE_NONNUMERIC)
	for comps in companies:
		wr.writerow(comps)

createCSV(records)