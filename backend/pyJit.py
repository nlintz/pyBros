import sys
from pySQL import *

class node(object):
	def __init__(self, row):
		self.id = row['id']
		self.jitid = row['jitid']
		self.name = row['name']
		self.adjacencies = []
		self.pid = None
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
	if n.is_parent():
		system = create_planets(n)
	return system
	
def create_planets(parent):
	system = []
	child_list = get_childs_by_pid(parent.id)
	for childs in child_list:
		row = get_node_by_id(childs['chid'])
		p = node(row)
		# p.pid = parent.id
		parent.add_child(p)
		planet_list.append(p)
		if p.is_parent():
			system.extend(create_planets(p))
		else:
			continue
	return system
	
def main(jitid):
	system = create_solar(jitid)
	print system

if __name__ == "__main__":
	main(sys.argv[1])