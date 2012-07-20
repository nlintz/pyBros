import urllib2
from bs4 import BeautifulSoup as bs
from lxml import etree
from HTMLParser import HTMLParser

categs = ['Ticker symbol', 'Company', 'GICS']

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'pyBros')]
response = opener.open("http://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
page = response.read()

bsoup = bs(page, "lxml")
companies = bsoup.find("table", {"class":"wikitable"})

table = str(companies)

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

print type(strip_tags(table))

# table = etree.XML(str(companies))
# rows = iter(table)
# 
# for col in next(rows):
# 	print col.title

# header = [col.text for col in next(rows)]
# print header