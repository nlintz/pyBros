import sys
from pySQL import *
import json
import os

class root_node(object):
	def __init__(self):
		self.id = 000
		self.name = 'blackhole'
		self.adjacencies = []
		self.data = {'name': self.name, 'ticker': 'ground zero', 'color': 333333,'dim':350 }
	def add_adjacent(self, universe):
		for systems in universe:
			for nodes in systems:
				if nodes.star:
					self.adjacencies.append(nodes.jitid)

class node(object):
	def __init__(self, row, star = False):
		"""
		initializes node object
		arg: row of SQL query data
		"""
		self.id = row['id']
		self.jitid = row['jitid']
		self.name = row['name']
		self.value = ['value']
		self.adjacencies = []
		self.pid = None
		self.dct = {}
		self.data = {}
		self.star = star
		self.is_star()
		
	def __repr__(self):
		return self.name
		return self.pid
		
	def is_star(self):
		if self.star:
			self.pid = 000
			
	def star_data(self,color_dict):
		self.data['ticker'] = self.jitid
		for n in self.adjacencies:
			if n.name == 'fin info':
				self.data['price'] = n.data['price']
				self.data['sector'] = n.data['sector']
				break
		self.prep_data(color_dict)
		
	def planet_data(self,color_dict):
		for n in self.adjacencies:
			self.data[n.name] = n.value
		self.prep_data(color_dict)
		self.adjacencies = []
	
	def add_child(self,n):
		"""
		adds child to adjacencies list
		"""
		self.adjacencies.append(n)
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
	def generate_adjacency_id(self):
		adj_id= []
		for childs in self.adjacencies:
			adj_id.append(childs.jitid)
		return adj_id
		
	def prep_data(self,color_dict):
	#	self.data['dim'] = 0.7*(float(self.data['price']))
		self.data['$color'] = color_dict[self.data['sector']]
		self.data['star'] = self.star
		
	def prep_JSON(self):
		self.dct = {
		'id':self.jitid,
		'name': self.name,
		'data': self.data,
		'adjacencies':self.generate_adjacency_id()
		}

def create_star(jitid):
	"""
	creates star/company
	args: requires companies jitID
	return: list of all nodes in system
	"""
	row = get_node_by_jitid(jitid)
	n = node(row, star = True)
	print n.name
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

def create_data(systems, color_dict):
	for nodes in systems:
		if nodes.star:
			ind = systems.index(nodes)
		else:
			nodes.planet_data(color_dict)
	systems[ind].star_data(color_dict)
	return systems
		
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

def write_json(universe, color_dict):
	for systems in universe:
		systems = create_data(systems, color_dict)
		create_JSON(systems)

def main(companies, color_dict):
	"""
	runs all functions
	args: list of jitids where jitid is ticker symbol of company
	prints json structure of node
	"""
	universe = create_universe(companies)
	print universe
	# write_json(universe, color_dict)
