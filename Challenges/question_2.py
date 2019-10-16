def advanced_sort(nodes_list):
    nodes = dict()
    for node in nodes_list:
        if node.value not in nodes.keys():
            nodes[node.value] = list()
        nodes[node.value].append(node)
    return [nodes[value] for value in sorted(nodes.keys(), reverse=True)]


assert advanced_sort([Node(1), Node(2), Node(1), Node(2)]) == [
    [Node(2), Node(2)], [Node(1), Node(1)]]
assert advanced_sort([Node(3), Node(2), Node(1), Node(2)]) == [
    [Node(3)], [Node(2), Node(2)], [Node(1)]]
