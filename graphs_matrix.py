from collections import deque

class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Vertex: {}>'.format(self.data)

    def __str__(self):
        return '<Vertex: {}>'.format(self.data)

# This is directed
class Graph:
    def __init__(self):
        # References to nodes, id - reference
        self.vertices = []
        self.size = len(self.vertices)

    def add_vertex(self, loc, value):
        self.size += 1
        for row in self.vertices:
            row.append(0)
        self.vertices.append([0 for i in range(self.size)])
        self.vertices[loc][loc] = 1


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



if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i, "Value here {}".format(i))
    print(g.vertices)
    # g.add_edge(0, 1)
    # g.add_edge(0, 2)
    # g.add_edge(0, 3)
    # g.add_edge(0, 4)
    # g.add_edge(0, 5)
    #
    # g.add_edge(1, 2)
    # g.add_edge(2, 0)
    # g.add_edge(2, 3)
    # g.add_edge(3, 3)
    # g.add_edge(3, 4)
    # g.add_edge(4, 5)


# test.add_edge(0, 1, 1)
# test.add_edge(1, 4, 1)
# test.add_edge(4, 6, 1)
# test.add_edge(3, 6, 2)
# test.add_edge(0, 3, 2)
# test.add_edge(3, 6, 1)
# test.add_edge(0, 6, 4)
