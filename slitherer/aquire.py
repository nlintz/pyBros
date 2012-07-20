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

class url_feeder(object):                                                       
	def __init__(self, fname):
		"""fname is the name of the file that we will have a url in
		each line representing a page for us to scrape."""
		self.queue = []
		with open(fname) as f:
			for l in f:
				self.insert(l)

	def __iter__(self):
		return self

	def next(self):
		if len(self.queue) != 0:
			return self.queue.pop()
		raise StopIteration

	def insert(self, url):
		self.queue.insert(0, url)

import mechanize as mech

class url_grabber(object):
	def __init__(self):
		self.br = mech.Browser()

	def retrieve(self, url):
		"""Attempt to retrieve the html stored at url."""
		try:
			self.br.open(url)
			return self.br.response().read()
		except:
			return 'Failed' # we should probably handle this...
		
