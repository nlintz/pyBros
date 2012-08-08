###############################################
# aquire.py
#
# This file is responsible for aquiring data
#  that is to be parsed.
#
# Dependencies:
#  mechanize
#
# 2012-07-19
# Trevor Pottinger
###############################################

import csv
wikibase = 'http://en.wikipedia.org/w/api.php'
wikiargs = '?action=query&format=xml&redirects&titles=%s'
wiki = wikibase + wikiargs

class url_feeder(object):                                                       
	def __init__(self, fname):
		"""fname is the name of the file that we will have a url in
		each line representing a page for us to scrape."""
		self.queue = []
		with open(fname) as f:
			reader = csv.DictReader(f)
			for l in reader:
				comp = l['company']
				comp = comp.replace(' ', '_')
				url = wiki % comp
				self.insert((url, l))

	def __iter__(self):
		return self

	def next(self):
		if len(self.queue) != 0:
			return self.queue.pop()
		raise StopIteration

	def insert(self, tup):
		"""tup is a tuple, where tup[0] is a url, tup[1] is a dict"""
		self.queue.insert(0, tup)

import mechanize as mech

class url_grabber(object):
	def __init__(self):
		self.br = mech.Browser()
		self.br.addheaders = [('User-agent', 'PyBro_Slitherer')]
		self.br.set_handle_robots(True)

	def retrieve(self, url):
		"""Attempt to retrieve the html stored at url."""
		try:
			self.br.open(url)
			return self.br.response().read()
		except:
			return 'Failed' # we should probably handle this...
		
	def toss_salad(self, fname):
		with open(fname) as f:
			pass
