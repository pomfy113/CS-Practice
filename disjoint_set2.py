

def test_cyclic(edges):
    highest = max(map(max, edges))
    parents = [i for i in range(highest + 1)]

    def find_parent(node):
        if parents[node] == node:
            return node
        else:
            return find_parent(parents[node])

    def union(node1, node2):
        node1_parent = find_parent(node1)
        node2_parent = find_parent(node2)

        if node1_parent == node2_parent:
            return False
        else:
            parents[node1_parent] = node2_parent
            return True

    for vtx, edge in edges:
        if not union(vtx, edge):
            return [vtx, edge]

    return []



test = [[1,2],[1,3],[2,4]]
cycle = test_cyclic(test)
print(cycle)
