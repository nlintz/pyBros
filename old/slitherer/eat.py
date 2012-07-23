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

def _gen_jitid(name, compname, ticker):
	if name == compname:
		return ticker
	else:
		m = md5()
		m.update('salt' + str(compname) + name)
		return m.hexdigest()

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

	def spoon(self, item):
		"""items are nodes, from prune"""
		con = self._connect()
		c = con.cursor()
		def esc(s):
			if s != None:
				return con.escape_string(str(s))
			else:
				return None
		query = """INSERT INTO nodes (name, jitid, value)
		VALUE ('%s', '%s', '%s');""" % \
		(esc(item.name), esc(item.jitid), esc(item.value))
		print query
		try:
			c.execute(query)
		except:
			con.close()
			return
		con.commit()
		query = """SELECT nid
		FROM nodes
		WHERE jitid='%s';""" % esc(item.jitid)
		print query
		try:
			c.execute(query)
		except:
			con.close()
			return
		row = c.fetchone()
		item.myid = row[0]
		print item.myid
		if item.pid != None:
			query = """INSERT INTO relations (pid, chid)
			VALUE ('%s', '%s');""" % (esc(item.pid), esc(item.myid))
			c.execute(query)
			con.commit()
			print query
		con.close()

	def eat(self, entree, sides):
		"""entree is a node from prune"""
		# add side dishes to main course
		for k, v in sides.iteritems():
			if k == 'ticker':
				ticker = v
			elif k == 'company':
				compname = v
				continue
			entree.adjacencies.append(node(k, v))
		# generate jitids
		course = node(compname, None)
		course.adjacencies.append(entree)
		course.jitid = _gen_jitid(compname, compname, ticker)
		entree.jitid = _gen_jitid(entree.name, compname, ticker)
		for submeal in entree.adjacencies:
			submeal.jitid = _gen_jitid(submeal.name, compname, ticker)
		# insert into mysql
		course.pid = None
		self.spoon(course)
		entree.pid = course.myid
		self.spoon(entree)
		for submeal in entree.adjacencies:
			submeal.pid = entree.myid
			self.spoon(submeal)
