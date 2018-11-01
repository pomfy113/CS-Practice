from collections import deque
class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = {} # TODO: Change key node ID to other node, Value: Weight

    def __repr__(self):
        return '<Vertex: {}>'.format(self.data)

    def __str__(self):
        return '<Vertex: {}>'.format(self.data)

# This is directed
class Graph:
    def __init__(self):
        # References to nodes, id - reference
        self.vertices = {}

    # Assume 1 weight
    def add_vertex(self, loc, value):
        self.vertices[loc] = Vertex(value)

    def add_edge(self, source, dest, weight=1):
        self.vertices[source].adjacent[dest] = weight

    def remove_vertex(self, vertex):
        self.vertices.pop(vertex)
        for _, value in self.vertices.items():
            if vertex in value.adjacent:
                value.adjacent.pop(vertex)

    def remove_edge(self, source, dest):
        self.vertices[source].adjacent.pop(dest)

    def print_graph(self):
        print(self.vertices)
        for id, vertex in self.vertices.items():
            print("Current node:", id)
            print("Adjacents:", vertex.adjacent)

    def depth_first(self, start, search):
        # Visited list, along with a stack
        visited = [None] * len(self.vertices)
        v_stack = []
        found = []

        # Initialize
        v_stack.append(start)

        # Main while loop; keep popping the stack
        while len(v_stack) > 0:
            loc = v_stack.pop()
            # Found
            if loc == search:
                return("DFS Iterative - Found {}! Route is: {}!\n".format(search, found))

            # If not visited, then we put it into the node print
            # NOW we should access for adjacencies
            if visited[loc] is not True:
                visited[loc] = True
                vertex = self.vertices[loc]
                for id, _ in vertex.adjacent.items():
                    v_stack.append(id)
                found.append(loc)


    def depth_first_recursive(self, index, search, visited=None, route=[]):
        if visited is None:
            visited = [None] * len(self.vertices)

        visited[index] = True
        vertex = self.vertices[index]
        print(index, vertex, vertex.data)
        if vertex.data == search:
            print("Found it")
            return("DFS Recursive - Found {}! Route is {}\n".format(search, route))

        route.append(vertex)

        for id, weight in vertex.adjacent.items():
            if visited[id] is not True:
                return self.depth_first_recursive(id, search, visited, route)

    def breadth_first(self, start, search):
        # Visited list, along with a stack
        visited = [None] * len(self.vertices)
        v_queue = deque()
        found = []

        v_queue.append(start)
        # Main while loop; keep popping the stack
        while v_queue:
            loc = v_queue.popleft()

            if loc == search:
                return("BFS - Found {}! Route is: {}!\n".format(search, found))

            # If not visited, then we put it into the node print
            if visited[loc] is not True:
                visited[loc] = True
                vertex = self.vertices[loc]
                for id, _ in vertex.adjacent.items():
                    v_queue.append(id)
                found.append(loc)


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i, "Value here {}".format(i))
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


    print("\nFirst, depth first. We should see 2, followed by 3->4->5, then 0->1 since that's left")
    print(g.depth_first(2, 5))
    print("Then breadth first. We should see 2 which has 0 and 3 since those are immediate adjacents, then go through 1, 4, 5.")
    print(g.breadth_first(2, 5))
    print("If we start with 0, we go through all of them in order since 0 is adjacent to all")
    print(g.breadth_first(0, 5))
    print("Now let's try depth first, but recursively")
    print(g.depth_first_recursive(2, 5))

    # print(g.nodes)
    g.print_graph()
    g.remove_edge(4, 5)
    print("\nRemoved, 4-5")
    g.print_graph()
    print("\nRemoved, vertex 1")
    g.remove_vertex(1)
    g.print_graph()

# test.add_edge(0, 1, 1)
# test.add_edge(1, 4, 1)
# test.add_edge(4, 6, 1)
# test.add_edge(3, 6, 2)
# test.add_edge(0, 3, 2)
# test.add_edge(3, 6, 1)
# test.add_edge(0, 6, 4)
