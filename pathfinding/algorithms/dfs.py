def dfs_traversal(graph, start):
    '''
    wrapper for _dfs_traversal that
    adds visited attribute to graph before
    starting recursive calls
    '''
    graph.add_attr('visited', default_val=False)
    _dfs_traversal(graph, start)

def _dfs_traversal(graph, start):
    start = graph.get_node(start)
    start.add_attr('visited', val=True)
    print(start.key)

    for edge in start:
        dst_node = graph.get_node(edge.dest_node)

        if not dst_node.attributes['visited']:
            _dfs_traversal(graph, edge.dest_node)
