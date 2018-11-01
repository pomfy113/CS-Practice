from collections import deque

# This is directed
class Graph:
    def __init__(self):
        # References to nodes, id - reference
        self.vertices = {}

    # Assume 1 weight
    def add_vertex(self, loc):
        self.vertices[loc] = []

    def add_edge(self, source, dest):
        if dest not in self.vertices[source]:
            self.vertices[source].append(dest)

    def remove_vertex(self, vertex):
        self.vertices.pop(vertex)

    def remove_edge(self, source, dest):
        self.vertices[source].adjacent.pop(dest)

    def print_graph(self):
        print(self.vertices)

    def dfs(self, start, search):
        visited = set([start])
        search_stack = []

        search_stack.append(start)

        while len(search_stack) > 0:
            next = search_stack.pop()
            visited.add(next)
            if next == search:
                print("Found {}".format(search))
                return True
            else:
                for adj in self.vertices[next]:
                    if adj not in visited:
                        search_stack.append(adj)

    def dfs_recursive(self, vertex, search, visited=None):
        if visited is None:
            visited = set([vertex])

        visited.add(vertex)

        if vertex == search:
            print("FOUND {}".format(search))
            return True

        for adj in self.vertices[vertex]:
            if adj not in visited:
                found = self.dfs_recursive(adj, search, visited)

                if found is True:
                    return

    def bfs(self, start, search):
        visited = set([start])
        search_stack = deque()

        search_stack.append(start)

        while len(search_stack) > 0:
            next = search_stack.popleft()
            visited.add(next)
            if next == search:
                print("Found {}".format(search))
                return True
            else:
                for adj in self.vertices[next]:
                    if adj not in visited:
                        search_stack.append(adj)

    def cycle_detect(self):
        for vtx in self.vertices:
            visited = set([])
            search_stack = []
            search_stack.append(vtx)

            while len(search_stack) > 0:
                index = search_stack.pop()

                if vtx in visited:
                    print("CYCLE FOUND - {}".format(vtx))
                    return
                else:
                    for adj in self.vertices[index]:
                        if adj not in visited:
                            visited.add(adj)
                            search_stack.append(adj)


if __name__ == "__main__":
    g = Graph()
    for i in range(7):
        g.add_vertex(i)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(0, 5)

    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.print_graph()

    print("Starting dfs")
    g.dfs(2, 3)
    print("= = = Starting recursive, should return= = = ")
    g.dfs_recursive(2, 3)
    print("= = = Continuing recursive, should be false= = = ")
    g.dfs_recursive(2, 6)
    print("= = = Starting bfs = = = ")

    g.bfs(2, 3)
    print("Cycle detection")
    g.cycle_detect()

    print("Let's try a different once")
    h = Graph()
    for i in range(7):
        h.add_vertex(i)
    h.add_edge(0, 1)
    h.add_edge(0, 2)
    h.add_edge(0, 3)
    h.add_edge(0, 4)
    h.add_edge(2, 4)
    h.add_edge(3, 4)
    h.add_edge(4, 5)

    h.cycle_detect()




# test.add_edge(0, 1, 1)
# test.add_edge(1, 4, 1)
# test.add_edge(4, 6, 1)
# test.add_edge(3, 6, 2)
# test.add_edge(0, 3, 2)
# test.add_edge(3, 6, 1)
# test.add_edge(0, 6, 4)
