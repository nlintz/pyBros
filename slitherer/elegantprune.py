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

def _paren(s):
	return '(%s)' % s

class data_extractor(object):                                                   
	STRUCTURES = ['div', 'table', 'tbody', 'body', 'ul', 'ol', 'dl', 'form']
	NARROWERS = ['li', 'dd', 'tr', 'td', 'th', 'thead', 'span', 'p']
	EMPHASIZERS = ['b', 'a', 'i', 'font', 'em', 'h1', 'h2', 'h3', 'h4',
			'h5', 'h6', 'small', 'strong', 'title']

	KEYWORDS = ['quote', 'market', 'title']
	parenkeywords = map(lambda s: '(%s)' % s, KEYWORDS)
	kwregex = re.compile('|'.join(parenkeywords))

	def __init__(self, feeder):
		self.feeder = feeder
		self._good_data = []

	def extract(self, html):
		"""Returns a list of annotated data we think is important."""
		self.soup = bs(html)
		self._relavence() # sets all _relavence to 0
		self._reduce1()
		self._reduce2()
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
		g = self.soup.recursiveChildGenerator()
		for elem in g:
			elem._relavence = 0

	def _reduce1(self):
		structuresdict = {}
		for tag in STRUCTURES:
			structuresdict[tag] = True
		tags = self.soup.findAll(structuresdict)
		for tag in tags:
			g = self.soup.recursiveChildGenerator()
			for elem in g:
				elem._relavence += 1

	def _reduce2(self):
		narrowersdict = {}
		for tag in NARROWERS:
			narrowersdict[tag] = True
		tags = self.soup.findAll(narrowersdict)
		for tag in tags:
			g = self.soup.recursiveChildGenerator()
			for elem in g:
				elem._relavence += 2
				tag._relavnce += elem._relavence

	def _annotate(self):
		pass

from difflib import SequenceMatcher as seqmatcher

def fuzzy(str1, str2):
	"""Returns some fuzzy string comparison of the two strings."""
	return seqmatcher(None, str1, str2).ratio()

class data_cleanser(object):
	def __init__(self):
		pass

	def polish(self, data):
		pass

