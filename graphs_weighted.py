from collections import deque
class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = {} # TODO: Change key node ID to other node, Value: Weight

    def __repr__(self):
        return '<Vertex {}>'.format(self.data)

    def __str__(self):
        return '<Vertex {}>'.format(self.data)

class Graph:
    def __init__(self, size):
        # TODO: References to nodes
        self.size = size
        self.vertices = {i:Vertex(i) for i in range(size)}

    # Assume 1 weight
    def add_vertex(self, source, dest, weight=1):
        self.vertices[source].adjacent[dest] = weight

    def print_graph(self):
        print(self.vertices)
        for id, vertex in self.vertices.items():
            print("Current node:", id)
            print("Adjacents:", vertex.adjacent)

    def depth_first(self, start):
        # Visited list, along with a stack
        visited = [None] * self.size
        v_stack = []
        v_print = []

        # Initializing
        vertex = self.vertices[start]
        visited[start] = True
        v_print.append(vertex.data)

        # Append links to other nodes
        for id, weight in vertex.adjacent.items():
            adjacent = self.vertices[id]
            v_stack.append(adjacent)

        # Main while loop; keep popping the stack
        # The stack makes us go deep before exploring the rest
        while len(v_stack) > 0:
            vertex = v_stack.pop()

            # If not visited, then we put it into the node print
            if visited[vertex.data] is not True:
                visited[vertex.data] = True
                for id, weight in vertex.adjacent.items():
                    adjacent = self.vertices[id]
                    v_stack.append(adjacent)
                v_print.append(vertex.data)
        print(v_print)

    def depth_first_recursive(self, id, visited=None):
        if visited is None:
            visited = [None] * self.size
            print(id)
        visited[id] = True
        vertex = self.vertices[id]
        for id, weight in vertex.adjacent.items():
            if visited[id] is not True:
                print(id)
                self.depth_first_recursive(id, visited)

    def breadth_first(self, start):
        # Visited list, along with a stack
        visited = [None] * self.size
        v_queue = deque()
        v_print = []

        # Initializing
        vertex = self.vertices[start]
        visited[start] = True
        v_print.append(vertex.data)

        # Append links to other nodes
        for id, weight in vertex.adjacent.items():
            adjacent = self.vertices[id]
            v_queue.append(adjacent)

        # Main while loop; keep popping the stack
        # The stack makes us go deep before exploring the rest
        while len(v_queue) > 0:
            vertex = v_queue.popleft()

            # If not visited, then we put it into the node print
            if visited[vertex.data] is not True:
                visited[vertex.data] = True
                for id, weight in vertex.adjacent.items():
                    adjacent = self.vertices[id]
                    v_queue.append(adjacent)
                v_print.append(vertex.data)
        print(v_print)


if __name__ == "__main__":
    g = Graph(6)
    g.add_vertex(0, 1)
    g.add_vertex(0, 2)
    g.add_vertex(0, 3)
    g.add_vertex(0, 4)
    g.add_vertex(0, 5)

    g.add_vertex(1, 2)
    g.add_vertex(2, 0)
    g.add_vertex(2, 3)
    g.add_vertex(3, 3)
    g.add_vertex(3, 4)
    g.add_vertex(4, 5)

    # print(g.nodes)
    g.print_graph()
    print("\nFirst, depth first. We should see 2, followed by 3->4->5, then 0->1 since that's left")
    g.depth_first(2)
    print("Then breadth first. We should see 2 which has 0 and 3 since those are immediate adjacents, then go through 1, 4, 5.")
    g.breadth_first(2)
    print("If we start with 0, we go through all of them in order since 0 is adjacent to all")
    g.breadth_first(0)

    g.depth_first_recursive(2)



# test.add_vertex(0, 1, 1)
# test.add_vertex(1, 4, 1)
# test.add_vertex(4, 6, 1)
# test.add_vertex(3, 6, 2)
# test.add_vertex(0, 3, 2)
# test.add_vertex(3, 6, 1)
# test.add_vertex(0, 6, 4)
