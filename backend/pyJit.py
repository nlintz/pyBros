import sys
from pySQL import *
import json

class node(object):
	def __init__(self, row, star):
		"""
		initializes node object
		arg: row of SQL query data
		"""
		self.id = row['id']
		self.jitid = row['jitid']
		self.name = row['name']
		self.adjacencies = []
		self.value = row['value']
		self.pid = None
		self.jit = None
		self.dct = {}
		self.is_star()
	def __repr__(self):
		return self.name
		return self.pid
	def is_star(self):
		if star:
			self.pid = 000
			self.adjacencies.append(self.pid)
	def add_child(self,n):
		"""
		adds child to adjacencies list
		"""
		self.adjacencies.append(n.jitid)
		n.pid = self.id			
	def is_parent(self):
		"""
		checks if node has children
		returns boolean
		"""
		if get_childs_by_pid(self.id):
			return True
		else:
			return False
	def generate_JSON(self):
		"""
		generates JSON structure
		returns JSON structure
		"""
		self.dct = {
		'jitid':self.jitid,
		'name': self.name,
		'data':{'value':self.value},
		'adjacencies':self.adjacencies
		}
		self.jit = json.dumps(self.dct)
		return self.jit
	def write_JSON(self, fName):
		"""
		writes json to file
		args: file name
		"""
		with open('%s.json' % (fName), 'rwb') as fp:
			json.dump(self.dct, fp)


def create_star(jitid):
	"""
	creates star/company
	args: requires companies jitID
	return: list of all nodes in system
	"""
	row = get_node_by_jitid(jitid)
	n = node(row, star = True)
	system = [n]
	if n.is_parent():
		system.extend(create_system(n))
	return system
	
def create_system(parent):
	"""
	creates childs of parent node recursively
	args: node object
	returns list of all children node for given parent node
	"""
	system = []
	child_list = get_childs_by_pid(parent.id)
	for childs in child_list:
		row = get_node_by_id(childs['chid'])
		p = node(row)
		parent.add_child(p)
		system.append(p)
		if p.is_parent():
			system.extend(create_system(p))
		else:
			continue
	return system

def create_universe(companies):
	universe =[]
	for jitid in companies:
		system = create_star(jitid)
		universe.append(system)
	return universe

def write_json(universe):
	for systems in universe:
		fName = systems[0].name
		for nodes in systems:
			nodes.write_JSON(fName)

def main(companies):
	"""
	runs all functions
	args: list of jitids where jitid is ticker symbol of company
	prints json structure of node
	"""
	universe = create_universe(companies)
	
	
	

if __name__ == "__main__":
	main(sys.argv[1])
