import MySQLdb

def _connect():
	return MySQLdb.connect(user='root', passwd='pybros', db='rev2')

# TODO clean node_id
def get_node_by_id(node_id):
	"""Returns a row that corresponds to the node with the matching
	node_id."""
	con = _connect()
	c = con.cursor()
	query = """SELECT * 
	FROM nodes
	WHERE id='%s';""" % node_id
	c.execute(query)
	match = c.fetchone()
	desc = [ desc[0] for desc in c.description ]
	con.close()
	return dict(zip(desc, match))

# TODO clean name
def get_node_by_jitid(jitid):
	"""Returns a row that corresponds to the node with the matching
	jitid."""
	con = _connect()
	c = con.cursor()
	query = """SELECT * 
	FROM nodes
	WHERE jitid='%s';""" % jitid
	c.execute(query)
	match = c.fetchone()
	desc = [ desc[0] for desc in c.description ]
	con.close()
	return dict(zip(desc, match))

def get_childs_by_pid(pid):
	"""Returns all the rows that correspond to the children with 
	parents that have id=pid."""
	con = _connect()
	c = con.cursor()
	query = """SELECT *
	FROM childs
	WHERE pid='%s';""" % pid
	num = c.execute(query) # num should be the number of matches
	desc = [ desc[0] for desc in c.description ]
	l = []
	for i in range(num):
		data = c.fetchone()
		l.append(dict(zip(desc, data)))
	con.close()
	return l
