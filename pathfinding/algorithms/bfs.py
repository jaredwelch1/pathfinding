from collections import deque

def bfs_traversal(graph, start):

	queue = deque()
	queue.append(start)
	
	while queue:
		node_key = queue.popleft()
		node = graph.get_node(node_key)
		print(node.key)
		for edge in node:
			queue.append(edge.dest_node)
