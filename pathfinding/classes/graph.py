from .node import Node

class Graph(object):
	'''
	A graph class representation for use with pathfindng algorithms. Will use hashable object
	as the key to identify nodes.

	edges will be represented by a dictionairy within each node, with the node the edge points to as the key
	and the weight of the edge represented by the value within the dictionary.

	The graph itself will be a dictionary of nodes. Each node will be an object, with a dict of edge/value pairs
	Node will also have a dictionary for node attributes, which will allow custom defined attributes to be defined
	and assigned (such as color, visited, etc)
	'''

	def __init__(self, key_list=None):
		'''
			Graph object constructor

			key_list: optional list of node keys to initialize the graph with

		'''

		self.nodes = {}

		if key_list is not None:
			self.insert_nodes(key_list)

	def __iter__(self):
		'''
			to make it easy to loop over nodes in the graph
			ex: for node in graph

			mostly should be used to label, add data, add attributes etc., to all nodes in graph.
			NOT really meant for traversal, as this pays no mind to edges, simply the order
			that they appear in the node dictionairy
		'''
		return iter([self.nodes[key] for key in self.nodes])

	def __len__(self):
		'''
			Will return the count of nodes in the graph.
		'''
		return len(self.nodes)

	def add_node(self, key):
		'''
			add single node to graph

			key - unique key to identify node (must be hashable object for valid dict key)
			node - node to add to graph

		'''
		self.nodes[key] = Node(key)

	def insert_nodes(self, key_list):

		'''
			add several nodes to graph

			key_list - a list of keys for nodes to be added to the graph
		'''
		for key in key_list:
			self.nodes[key] = Node(key)

	def add_edge(self, src_key, dst_key, weight=None):
		'''
			add an edge between two nodes

			src_key - key for node that edge starts at
			dst_key - key for node that edge ends at
			weight 	- optional argument to assign a weight to an edge

		'''

		if src_key in self.nodes and dst_key in self.nodes:
			src_node = self.nodes[src_key]
			src_node.attach_edge(dst_key, weight)

	def get_node(self, key):
		'''
			get the node identified by key
		'''
		if key in self.nodes:
			return self.nodes[key]
		else:
			return None
