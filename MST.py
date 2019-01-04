import heapq

def adj_dict(data):
    graph = {}
    for vtx, adj, weight in data:
        if vtx not in graph:
            graph[vtx] = {adj: weight}
        else:
            graph[vtx][adj] = weight
        if adj not in graph:
            graph[adj] = { vtx: weight }
        else:
            graph[adj][vtx] = weight
    return graph

def prims(graph):
    data = {vtx: float('inf') for vtx in graph}
    data[0] = 0
    queue = [(0, 0)]
    visited = set()

    heapq.heapify(queue)

    while queue:
        weight, vtx = heapq.heappop(queue)

        if vtx not in visited:
            visited.add(vtx)

            for adj in graph[vtx]:
                adj_weight = graph[vtx][adj]

                if data[adj] > adj_weight:
                    data[adj] = adj_weight

                heapq.heappush(queue, (adj_weight, adj))
    return data

def kruskal(data):
    def cycle_detect(MST, next):
        MST_copy = [i for i in MST] + [next]
        max_node = max(map(max, MST_copy))
        parents = [i for i in range(max_node + 1)]

        def find_parent(node):
            if parents[node] == node:
                return node
            else:
                return find_parent(parents[node])

        def cycle(node1, node2):
            # Create union
            node1_parent = find_parent(node1)
            node2_parent = find_parent(node2)

            # Same parent? Cycle
            if node1_parent == node2_parent:
                return True
            else:
                # Union!
                parents[node1_parent] = node2_parent
                return False

        for _, vtx, adj in MST_copy:
            # If we find a cycle, stop
            if cycle(vtx, adj):
                return True

        return False

    queue = []
    graph = adj_dict(data)
    max_size = set()
    heapq.heapify(queue)

    for vtx, adj, weight in data:
        heapq.heappush(queue, (weight, vtx, adj))
        max_size.add(vtx)
        max_size.add(adj)

    max_size = max(max_size)
    visited = set()
    MST = []

    while len(MST) < max_size:
        next = heapq.heappop(queue)
        print(next)
        print(MST)
        if cycle_detect(MST, next) is False:
            MST.append(next)

    print(MST)

data = [
    (0, 1, 4),(0, 7, 8),(1, 7, 11),(1, 2, 8),
    (7, 8, 7),(7, 6, 1),(2, 8, 2),(2, 3, 7),
    (2, 5, 4),(8, 6, 6),(6, 5, 2),(3, 5, 14),
    (3, 4, 9),(5, 4, 10),
]

graph = adj_dict(data)
print(prims(graph))
print(kruskal(data))
