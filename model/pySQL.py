import MySQLdb

def _connect():
	return MySQLdb.connect(user='root', passwd='pybros', db='rev3')

# TODO clean node_id
def get_node_by_id(node_id):
	"""Returns a row that corresponds to the node with the matching
	node_id."""
	con = _connect()
	c = con.cursor()
	query = """SELECT * 
	FROM nodes
	WHERE nid='%s';""" % node_id
	c.execute(query)
	match = c.fetchone()
	desc = [ desc[0] for desc in c.description ]
	con.close()
	if match == None:
		return {}
	return dict(zip(desc, list(match)))

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
	if match == None:
		return {}
	return dict(zip(desc, list(match)))

def get_childs_by_pid(pid):
	"""Returns all the rows that correspond to the children with 
	parents that have nid=pid."""
	con = _connect()
	c = con.cursor()
	query = """SELECT *
	FROM relations 
	WHERE pid='%s';""" % pid
	num = c.execute(query) # num should be the number of matches
	desc = [ desc[0] for desc in c.description ]
	l = []
	for i in range(num):
		data = c.fetchone()
		l.append(dict(zip(desc, data)))
	con.close()
	return l

def get_parent_by_chid(chid):
	"""Returns the row that corresponds to the parent of the node
	with id=chid."""
	con = _connect()
	c = con.cursor()
	#query = """SELECT nodes.id, nodes.name, nodes.jitid, nodes.value
	query = """SELECT nodes.*
	FROM nodes
	INNER JOIN childs
	ON nodes.nid=relations.pid
	WHERE relations.chid='%s';""" % chid
	c.execute(query)
	match = c.fetchone()
	desc = [ desc[0] for desc in c.description ]
	con.close()
	if match == None:
		return {}
	return dict(zip(desc, list(match)))
