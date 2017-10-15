# TODO

## Add these into a separate algorithms part of either the graph class itself, or into an algortihms directory 

from graph import graph as Graph
from collections import deque

def dfs_traversal(graph, start):
	start = graph.get_node(start)
	
	print(start.key)

	for edge in start:
		#print(edge)
		dfs_traversal(graph, edge.dest_node)
	 
	
def bfs_traversal(graph, start):

	queue = deque()
	queue.append(start)
	
	while queue:
		node_key = queue.popleft()
		node = graph.get_node(node_key)
		print(node.key)
		for edge in node:
			queue.append(edge.dest_node)

if __name__ == "__main__":
	
	g = Graph([1, 2, 3, 4, 5, 6, 7, 8])
	g.add_edge(1, 2)
	g.add_edge(1, 3)
	g.add_edge(2, 4)
	g.add_edge(3, 5)
	g.add_edge(4, 6)
	g.add_edge(5, 7)
	g.add_edge(6, 8)

	dfs_traversal(g, 1)
	
	print('BFS for graph: ')
	bfs_traversal(g, 1)
