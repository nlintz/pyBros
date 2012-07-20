import urllib2
from BeautifulSoup import BeautifulSoup as bs
from HTMLParser import HTMLParser
import csv
import sys
import re

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


def get_table_soup(link):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'pyBros')]
	response = opener.open(link)
	page = response.read()

	bsoup = bs(page)
	table = bsoup.find("table", {"class":re.compile("wikitable")})
	return table


def get_company_list(table):
	records = []
	indices = []
	comps = table.findAll('tr')

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
	for i in range(len(records[0])):
		if records[0][i] == 'Ticker symbol':
			records[0][i] = 'ticker'
		elif records[0][i] == 'Company':
			records[0][i] = 'company'
		elif records[0][i] == 'GICS Sector':
			records[0][i] = 'sector'
	for i in range(len(records)):
		if i == 0:
			records[i].append('url')
		else:
			url = "http://finance.yahoo.com/q?s=%s" % (records[i][0])
			records[i].append(url)
	return records


def createCSV(companies, header = False):
	if not header:
		del companies[0]
	myFile = open('sp500.csv','wb')
	wr = csv.writer(myFile, quoting = csv.QUOTE_NONNUMERIC)
	for comps in companies:
		wr.writerow(comps)

def main():
	table = get_table_soup("http://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
	companies = get_company_list(table)
	createCSV(companies, True)

if __name__ == '__main__':
	main() 
	
