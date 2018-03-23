class Edge(object):
	'''
	Simple edge class to store edge weight and the key of the node that the edge points to
	'''

	def __init__(self, dest_key, weight=None):
		self.dest_node = dest_key
		self.weight = weight
	def __str__(self):
		return '(' + str(self.dest_node) + ', ' + str(self.weight) + ')'
	def __repr__(self):
		return '(' + str(self.dest_node) + ', ' + str(self.weight) + ')'

class Node(object):
	'''
	Each node will be an object, with a list of edge objects

	Edges represented by the key of the node the edge points to
	For example:
		nodes = A, B, C
		A -> B has weight of 4
		A -> C has weight of 10
		if A has an edge with B and C, then A.edges = [edge(B, 4), edge(C, 10)]


	Node will also have a dictionary for node attributes, which will allow custom defined attributes to be defined
	and assigned (such as color, visited, etc)
	'''

	def __init__(self, key, attribute_list=None):

		self.edges = []
		self.attributes = {}
		self.key = key


		if attribute_list is not None:
			for attr in attribute_list:
				self.attributes[attr] = ''
	def __iter__(self):
		'''
			This iteration returns a 2 item dictionary for each edge which contains
			the weight of the edge and the key of the destination node the edge points to

			Might be a better way, but was easiest way to return the data I neeeded

			Maybe could make a small edge class which just has two fields and use a list of
			edge objects rather than a dictionary...
		'''

		return iter(self.edges)


	def add_attr(self, attr, val=None):
		if val is not None:
			self.attributes[attr] = val
		else:
			self.attributes[attr] = None

	def has_attr(self, attr):
		return attr in self.attributes

	def attach_edge(self, dest_node_key, weight=None):
		self.edges.append(Edge(dest_node_key, weight))

	''' TODO: add insert_edges() which takes in a dict of key:weight pairs (key of destination node from src node) '''

	def __str__(self):
		return 'Node ' + str(self.key) + ' -> edges: ' + str(self.edges) + ' attributes: ' + str(self.attributes)
