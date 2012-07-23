import MySQLdb

def connect():
	"""Returns the MySQLdb cursor object."""
	con = MySQLdb.connect(user='root', passwd='pybros', db='rev1')
	return con.cursor()

#def use(cur, db_name):
#	"""Uses the database specified by db_name."""
#	pass

def get_one(cur, query):
	"""Returns a single match based on the query. If more
	than one match exists, return an error"""
	nummatches = cur.execute(query)
	return cur.fetchone()

def get_more(cur, query):
	"""Returns one or more matches based on the query."""
	nummatches = cur.execute(query)
	l = []
	match = cur.fetchone()
	while match != None:
		l.append(match)
		match = cur.fetchone()
	return l
