###############################################
# slitherer.py
#
# This is PyBros' data 'slitherer', cause we
#  don't crawl, we slither.
#  
# 2012-07-19
# Trevor Pottinger
###############################################

from aquire import url_feeder, url_grabber
from prune import data_extractor, data_cleanser
from eat import database_feeder

class slitherer(object):
	def __init__(self):
		self.feeder = url_feeder('sp500.csv')
		self.grabber = url_grabber()
		self.extractor = data_extractor(self.feeder)
		self.cleaner = data_cleanser()
		self.eater = database_feeder('pybros', 'getIn2it', 'rev3')

	def slither(self):
		i = 0
		for (url,appetizer) in self.feeder:
			i += 1
			print i
			xml = self.grabber.retrieve(url)
			if xml == '':
				continue # maybe something else?
			datalist = self.extractor.extract(xml)
			dinner = self.cleaner.cook(datalist)
			self.eater.eat(dinner, appetizer)

def main():
	pybros = slitherer()
	pybros.slither()

if __name__ == '__main__':
	main()
