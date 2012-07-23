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
		#self._reduce1()
		#self._reduce2()
		self._reduce3()
		self._annotate()
		self._wash()
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
		# grab all the cols that relate to fin info
		self._cols = self.soup.findAll(attrs={'class':'yfnc_tabledata1'})
		self._headers = [ col.previous for col in self._cols ]

	def _annotate(self):
		texts = [ col.text for col in self._cols ]
		self._ok_data = zip(self._headers, texts)

	# TODO don't depend on indicies
	def _wash(self):
		"""Clean the attributes to fit the `fin info' planet better"""
		self._good_data = range(8)
		for i in range(len(self._ok_data)):
			if i == 7:
				self._good_data[0] = ('range', self._ok_data[i][1])
			elif i == 8:
				self._good_data[1] = ('52wk_range', self._ok_data[i][1])
			elif i == 12:
				self._good_data[2] = ('P/E', self._ok_data[i][1])
			elif i == -1: # unimplemented thus far
				self._good_data[3] = ('dividends', self._ok_data[i][1])
			elif i == 11:
				self._good_data[4] = ('mkt_cap', self._ok_data[i][1])
			elif i == 9:
				self._good_data[5] = ('volume', self._ok_data[i][1])
			elif i == 10:
				self._good_data[6] = ('avg_volume', self._ok_data[i][1])
			elif i == 0: # realistically this is yesterdays price...
				self._good_data[7] = ('price', self._ok_data[i][1])

from difflib import SequenceMatcher as seqmatcher

def fuzzy(str1, str2):
	"""Returns some fuzzy string comparison of the two strings."""
	return seqmatcher(None, str1, str2).ratio()

class node(object):
	"""This is to mimic the node class from pyJit."""
	def __init__(self, name, value):
		self.id = None # not yet defined
		self.jitid = None # not yet calculated
		self.name = name
		self.adjacencies = []
		self.value = value
		self.pid = None

	def __repr__(self):
		return self.name

class data_cleanser(object):
	def __init__(self):
		pass

	def cook(self, datalist):
		"""This is going to return a python representation of a
		planet, not a solar system."""
		planet = node('fin info', None)
		for tup in datalist:
			if type(tup) != tuple:
				continue
			planet.adjacencies.append(node(tup[0], tup[1]))
		return planet

