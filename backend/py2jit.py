import sys
from pySQL import *
import json
import os

class node(object):
	def __init__(self, row):
		self.id = row['nid']
		self.jitid = row['jitid']
		self.name = row['name']
		self.value = row['value']
		self.data = {}

class star(node, ticker):
	def __init__(self):
		super(node, self, row).__init__()
		self.adj = []
	def is_star(self):
		return True
	def get_data(self, color_dict):
		for planets in self.adj:
			if planets.name == 'fin info'
				self.data['price'] = planets.data['price']
				self.data['ticker'] = planets.data['ticker']
				break
	def get_children(self):
		pl = get_childs_by_pid(self.id)
		for rows in pl:
			self.adj.append(planet(rows, self.jitid))
		return self.adj
	def get_adj_id(self):
		adj_id =[]
		for adj in self.adj:
			adj_id.append(adj.jitid)
		return adj_id
		

class planet(node, jittid):
	def __init__(self):
		super(node, self, row).__init__()
	def get_data(self, color_dict):
		attr_list = get_childs_by_pid(self.id)
		for attr in attr_list:
			dat = get_node_by_id(attr['chid'])
			self.data[dat['name']]:dat['value']

def main(companies, color_dict):
	universe = []
	for tickers in companies:
		row = get_node_by_jitid(ticker)
		st = star(row)
		st.get_children()
		for pl in st.adj:
			pl.get_data(color_dict)
		universe.append(st)
	print universe