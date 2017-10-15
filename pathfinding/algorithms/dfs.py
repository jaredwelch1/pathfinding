import sys
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__name__), '..')))

#from classes import graph

def dfs_traversal(graph, start):
	start = graph.get_node(start)
	
	print(start.key)

	for edge in start:
		#print(edge)
		dfs_traversal(graph, edge.dest_node)


