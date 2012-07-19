import csv
import json

class Node(dict):
    def __init__(self, (nid, name, ndescr)):
        dict.__init__(self)
        self['id'] = nid
        self['name'] = name.lstrip()
        self['description'] = ndescr.lstrip()
        self['children'] = []

    def add_node(self, node):
        for child in self['children']:
            if child.is_parent(node):
                child.add_node(node)
                break
        else:
            self['children'].append(node)

    def is_parent(self, node):
        if len(self['id']) == 4 and self['id'][-1] == '0':
            return node['id'].startswith(self['id'][:-1])
        return node['id'].startswith(self['id'])

class RootNode(Node):
    def __init__(self):
        Node.__init__(self, ('Root', '', ''))

    def is_parent(self, node):
        return True

def pretty_print(node, i=0):
    print '%sID=%s NAME=%s %s' % ('\t' * i, node['id'], node['name'], node['description'])
    for child in node['children']:
        pretty_print(child, i + 1)

def main():
    with open('input.csv') as f:
        f.readline() # Skip first line
        root = RootNode()
        for node in map(Node, csv.reader(f)):
            root.add_node(node)

    pretty_print(root)
    print json.dumps(root)

if __name__ == '__main__':
    main()
