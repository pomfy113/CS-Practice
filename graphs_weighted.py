from collections import deque
class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = {} # TODO: Change key node ID to other node, Value: Weight

    def __repr__(self):
        return '<Vertex {}>'.format(self.data)

    def __str__(self):
        return '<Vertex {}>'.format(self.data)

# This is directed
class Graph:
    def __init__(self):
        # TODO: References to nodes
        self.vertices = {}

    # Assume 1 weight
    def add_vertex(self, loc):
        self.vertices[loc] = Vertex(loc)

    def add_edge(self, source, dest, weight=1):
        self.vertices[source].adjacent[dest] = weight

    def remove_edge(self, source, dest):
        self.vertices[source].adjacent.pop(dest)

    def print_graph(self):
        print(self.vertices)
        for id, vertex in self.vertices.items():
            print("Current node:", id)
            print("Adjacents:", vertex.adjacent)

    def depth_first(self, start):
        # Visited list, along with a stack
        visited = [None] * len(self.vertices)
        v_stack = []
        v_print = []

        # Initialize
        # Originally, this was actually using pointers
        v_stack.append(start)

        # Main while loop; keep popping the stack
        # The stack makes us go deep before exploring the rest
        while len(v_stack) > 0:
            loc = v_stack.pop()
            # If not visited, then we put it into the node print
            # NOW we should access for adjacencies
            print(loc, visited)
            if visited[loc] is not True:
                visited[loc] = True
                vertex = self.vertices[loc]
                for id, _ in vertex.adjacent.items():
                    v_stack.append(id)
                v_print.append(loc)
        print(v_print)

    def depth_first_recursive(self, id, visited=None):
        if visited is None:
            visited = [None] * len(self.vertices)
            print(id)

        visited[id] = True
        vertex = self.vertices[id]
        for id, weight in vertex.adjacent.items():
            if visited[id] is not True:
                print(id)
                self.depth_first_recursive(id, visited)

    def breadth_first(self, start):
        # Visited list, along with a stack
        visited = [None] * len(self.vertices)
        v_queue = deque()
        v_print = []

        v_queue.append(start)
        # Main while loop; keep popping the stack
        while v_queue:
            loc = v_queue.popleft()
            # If not visited, then we put it into the node print
            if visited[loc] is not True:
                visited[loc] = True
                vertex = self.vertices[loc]
                for id, _ in vertex.adjacent.items():
                    v_queue.append(id)
                v_print.append(loc)
        print(v_print)


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
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



    # print(g.nodes)
    g.print_graph()
    g.remove_edge(4, 5)
    g.print_graph()

    # print("\nFirst, depth first. We should see 2, followed by 3->4->5, then 0->1 since that's left")
    # g.depth_first(2)
    # print("Then breadth first. We should see 2 which has 0 and 3 since those are immediate adjacents, then go through 1, 4, 5.")
    # g.breadth_first(2)
    # print("If we start with 0, we go through all of them in order since 0 is adjacent to all")
    # g.breadth_first(0)
    #
    # g.depth_first_recursive(2)



# test.add_edge(0, 1, 1)
# test.add_edge(1, 4, 1)
# test.add_edge(4, 6, 1)
# test.add_edge(3, 6, 2)
# test.add_edge(0, 3, 2)
# test.add_edge(3, 6, 1)
# test.add_edge(0, 6, 4)
