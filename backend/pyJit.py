import sys
from pySQL import *
import json
import os

class node(object):
	def __init__(self, row, star = False):
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
		self.is_star(star)
	def __repr__(self):
		return self.name
		return self.pid
	def is_star(self,star):
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

def create_JSON(systems):
	for nodes in systems:
		if nodes.pid == 000:
			ind = systems.index(nodes)
			fName = systems[ind].name + ".json"
			break
	fp = open(fName, 'w')
	for nodes in systems:
		nodes.generate_JSON()
		json.dump(nodes.dct,fp)
		fp.write('\n')
	fp.close()

def write_json(universe):
	for systems in universe:
		create_JSON(systems)

def main(companies):
	"""
	runs all functions
	args: list of jitids where jitid is ticker symbol of company
	prints json structure of node
	"""
	if type(companies) != list:
		companies = [companies]
	universe = create_universe(companies)	
	write_json(universe)
	
if __name__ == "__main__":
	main(sys.argv[1])
