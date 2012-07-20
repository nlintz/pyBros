###############################################
# eat.py
#
# This file will work on feeding processed data
#  to the database, it may need some utensils
#
# 2012-07-19
# Trevor Pottinger
###############################################

from hashlib import md5

def _gen_jitid(name, element_id, ticker):
	if name == 'ticker':
		return ticker
	else:
		m = md5()
		m.update('salt' + str(element_id) + name)
		return m.hexdigest()

from prune import node

class database_feeder(object):
	def __init__(self, uname, passwd, dbname):
		pass

	def eat(self, entree, sides):
		for k, v in sides.iteritems():
			entree.adjacencies.append(node(k, v))
