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
	def __init__(self, row, tag = 'planet'):
		"""
		initializes node object
		arg: row of SQL query data
		"""
		self.id = row['nid']
		self.jitid = row['jitid']
		self.name = row['name']
		self.value = row['value']
		self.adjacencies = []
		self.pid = None
		self.dct = {}
		self.data = {}
		
	def add_child(self,n):
		"""
		adds child to adjacencies list
		"""
		self.adjacencies.append(n.id)
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
		
	def prep_data(self,color_dict):
		self.data['dim'] = 0.7*(float(self.data['price']))
		self.data['$color'] = color_dict[self.data['sector']]
		self.data['star'] = self.star
		
	def prep_JSON(self):
		self.dct = {
		'id':self.jitid,
		'name': self.name,
		'data': self.data,
		'adjacencies':self.adjecencies()
		}

def create_star(ticker):
	row = get_node_by_jitid(ticker)
	n = node(row, 'star')
	print n
	system = [n]
	print n.is_parent()
	if n.is_parent:
		system.extend(create_system(n))
	return system
	
def create_system(parent):
	"""
	creates childs of parent node recursively
	args: node object
	returns list of all children node for given parent node
	"""
	system = []
	print parent.name
	child_list = get_childs_by_pid(parent.id)
	if parent.name != 'fin info':		
		for childs in child_list:
			row = get_node_by_id(childs['chid'])
			p = node(row,'planet')
			p.add_child(parent)
			parent.add_child(p)
			system.append(p)
	else:
		for child in  child_list:
			parent.data[child['name']] = child['value']
		system.append(parent)
	return system

def create_universe(companies):
	universe =[]
	for jitid in companies:
		system = create_star(jitid)
		universe.append(system)
	return universe

def createData(universe, color_dict):
	for system in universe:
		for n in system:
			n.prep_data(color_dict)
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

def write_json(universe, color_dict):
	for systems in universe:
		create_JSON(systems)

def main(companies, color_dict):
	"""
	runs all functions
	args: list of jitids where jitid is ticker symbol of company
	prints json structure of node
	"""
	universe = create_universe(companies)
	universe1 = createData(universe, color_dict)
	write_json(universe1)
