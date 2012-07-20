import sys
from pySQL import *

class node(object):
	def __init__(self, row):
		self.id = row['id']
		self.jitid = row['jitid']
		self.name = row['name']
		self.adjacencies = []
		self.value = row['value']
		self.pid = None
	def __repr__(self):
		return self.name
	def add_child(self,n):
		self.adjacencies.append(n.jitid)
		n.pid = self.id			
	def is_parent(self):
		if get_childs_by_pid(self.id):
			return True
		else:
			return False

def create_solar(jitid):
	row = get_node_by_jitid(jitid)
	n = node(row)
	system = [n]
	if n.is_parent():
		system.extend(create_planets(n))
	return system
	
def create_planets(parent):
	system = []
	child_list = get_childs_by_pid(parent.id)
	for childs in child_list:
		row = get_node_by_id(childs['chid'])
		p = node(row)
		parent.add_child(p)
		system.append(p)
		if p.is_parent():
			system.extend(create_planets(p))
		else:
			continue
	return system
	
def main(jitid):
	system = create_solar(jitid)
	d = {}
	for s in system:
		d[s.jitid] = s.adjacencies
	print d

if __name__ == "__main__":
	main(sys.argv[1])
