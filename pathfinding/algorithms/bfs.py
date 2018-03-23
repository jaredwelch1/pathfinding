from collections import deque

def bfs_traversal(graph, start):
    graph.add_attr('visited', default_val=False)
    queue = deque()
    queue.append(start)

    while queue:
        node_key = queue.popleft()

        node = graph.get_node(node_key)
        node.add_attr('visited', val=True)
        print(node.key)

        for edge in node:
            dest_node = graph.get_node(edge.dest_node)
            if not dest_node.attributes['visited']:
                queue.append(edge.dest_node)
