###############################################
# eat.py
#
# This file will work on feeding processed data
#  to the database, it may need some utensils
#
# 2012-07-31
# Trevor Pottinger
###############################################

from hashlib import md5

def _gen_jitid(name, compname, ticker):
	if name == 'company':
		return ticker
	else:
		m = md5()
		m.update('salt' + str(compname) + name)
		return m.hexdigest()

def _clean(string):
	if string == None:
		return ''
	return string.replace('\'', '').replace(';', '')

from prune import node
import MySQLdb

class database_feeder(object):
	def __init__(self, uname, passwd, dbname):
		self.uname = uname
		self.passwd = passwd
		self.dbname = dbname

	def _connect(self):
		u = self.uname
		p = self.passwd
		d = self.dbname
		return MySQLdb.connect(user=u, passwd=p, db=d)

	# TODO clean item names and values
	def spoon(self, item):
		"""items are nodes, from prune"""
		con = self._connect()
		c = con.cursor()
		cleaned_item = (_clean(item.name), _clean(item.jitid), _clean(item.value))
		query = """INSERT INTO nodes (name, jitid, value)
VALUE ('%s', '%s', '%s');""" % cleaned_item
		#print query
		# this is where the exception occured
		c.execute(query)
		con.commit()
		query = """SELECT nid
		FROM nodes
		WHERE jitid='%s';""" % item.jitid
		#print query
		c.execute(query)
		row = c.fetchone()
		item.myid = row[0]
		if item.pid != None:
			query = """INSERT INTO relations (pid, chid)
VALUE ('%s', '%s');""" % (item.pid, item.myid)
			c.execute(query)
			con.commit()
			#print query
		con.close()

	def eat(self, entree, sides):
		"""entree is a node from prune"""
		# add side dishes to main course
		for k, v in sides.iteritems():
			if k == 'ticker':
				ticker = v
			elif k == 'company':
				compname = v
			entree.adjacencies.append(node(k, v))
		# generate jitids
		entree.jitid = _gen_jitid(entree.name, compname, ticker)
		for submeal in entree.adjacencies:
			submeal.jitid = _gen_jitid(submeal.name, compname, ticker)
		# insert into mysql
		entree.pid = None
		self.spoon(entree)
		for submeal in entree.adjacencies:
			submeal.pid = entree.myid
			self.spoon(submeal)
