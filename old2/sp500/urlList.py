import csv
import sys

def create_yfinance_url(f_name):
	url_list = []
	reader = csv.reader(open(f_name, 'r'))
	for rows in reader:
		url = "http://finance.yahoo.com/q?s=%s" % (rows[0])
		url_list.append(url)
	return url_list

def create_csv_with_urls(f_name):
	csv.DictReader(f_name)

def main(f_name = 'sp500.csv'):
	a = create_yfinance_url(f_name)
	print a

if __name__ == '__main__':
	main(*sys.argv)
