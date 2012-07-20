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

	def _reduce1(self):
		pass

	def _reduce2(self):
		pass

	def _reduce3(self):
		pass

	def _annotate(self):
		pass

	def _wash(self):
		pass

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

