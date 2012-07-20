import sys
import 
from pySQL import *
import json

class node(object):
	def __init__(self, row):
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
		self.d = {}
	def __repr__(self):
		return self.name
		return self.pid
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
		self.d = {
		'jitid' : self.jitid
		'name'  : self.name
		'data'  : {'value':self.value}
		'adjacencies' : self.adjacencies
		}
		self.jit = JSON.dumps(d)
		return self.jit
	def write_JSON(self, fName):
		"""
		writes json to file
		args: file name
		"""
		with open('%s.json' % (fName), 'wb') as fp:
			json.dump(self.d, fp)

def create_star(jitid):
	"""
	creates star/company
	args: requires companies jitID
	return: list of all nodes in system
	"""
	row = get_node_by_jitid(jitid)
	n = node(row)
	system = [n]
	if n.is_parent():
		system.extend(create_planets(n))
	return system
	
def create_planets(parent):
	"""
	creates childs of parent node recursively
	args: parent node
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
			system.extend(create_planets(p))
		else:
			continue
	return system
	
def main(jitid):
	system = create_solar(jitid)
	for i in range(len(system)):
		system[i] = system[i].generate_JSONk

if __name__ == "__main__":
	main(sys.argv[1])
