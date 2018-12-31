def find_parent(parent, i):
    if parent[i] == -1:
        return i
    else:
        return find_parent(parent, parent[i])

def union(parent, node, edge):
    x = find_parent(parent, node)
    y = find_parent(parent, edge)
    parent[x] = y

def test_cyclic(dict):
    parent = { node: -1 for node in dict }

    for node, edges in dict.items():
        for edge in edges:
            print(parent)
            node_parent = find_parent(parent, node)
            edge_parent = find_parent(parent, edge)

            if node_parent == edge_parent:
                print("Cycle")
                return True
            union(parent, node_parent, edge_parent)

test1 = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]
}

test2 = {
    1: [2, 3],
    2: [],
    3: []
}

test_cyclic(test2)
