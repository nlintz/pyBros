###############################################
# prune.py
#
# This file will extract only the useful info
#  and then clean it so we can eat it.
#
# 2012-07-19
# Trevor Pottinger
###############################################

from BeautifulSoup import BeautifulSoup as bs
import re

class data_extractor(object):
	STRUCTURES = ['table', 'div']

	KEYWORDS = ['quote', 'market', 'title']
	parenkeywords = map(lambda s: '(%s)' % s, KEYWORDS)
	kwregex = re.compile('|'.join(parenkeywords))

	def __init__(self, feeder):
		self.feeder = feeder
		self._good_data = []

	def extract(self, html):
		"""Returns a list of annotated data we think is important."""
		self.soup = bs(html)
		self._reduce1()
		self._reduce2()
		self._reduce3()
		self._annotate()
		return self._good_data

	def _depth(self, elem):
		"""Returns the max distance from elem to a leaf"""
		if elem.contents == []:
			return 1
		depths = []
		for child in elem.contents:
			depths.append(self._depth(child))
		return 1 + max(depths)

	def _distance(self, elem1, elem2):
		pass

	def _relavence(self):
		pass

	def _reduce1(self):
		structuredict = {}
		for tag in data_extractor.STRUCTURES:
			structuredict[tag] = True
		self._tables = self.soup.findAll(structuredict)
		print 'tables: %s' % len(self._tables)

	def _reduce2(self):
		self._rows = []
		for tbl in self._tables:
			rows = tbl.findAll({'tr':True})
			self._rows += rows
		print 'rows: %s' % len(self._rows)

	def _reduce3(self):
		self._headers = []
		self._cols = []
		for row in self._rows:
			headers = row.findAll({'th':True})
			cols = row.findAll({'td':True})
			for header in headers:
				if header.contents == []:
					self._headers.append(header)
			for col in cols:
				if col.contents == []:
					self._cols.append(col)
		print 'headers: %s' % len(self._headers)
		print 'cols: %s' % len(self._cols)

	def _annotate(self):
		self._good_data = zip(self._headers, self._cols)

from difflib import SequenceMatcher as seqmatcher

def fuzzy(str1, str2):
	"""Returns some fuzzy string comparison of the two strings."""
	return seqmatcher(None, str1, str2).ratio()

class data_cleanser(object):
	def __init__(self):
		pass

	def cook(self, datalist):
		pass

