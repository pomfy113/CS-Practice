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
        self.vertices_ids = {}

        self.size = len(self.vertices)

    def add_vertex(self, loc, id):
        self.size += 1
        for row in self.vertices:
            row.append(0)
        self.vertices.append([0 for i in range(self.size)])
        self.vertices[loc][loc] = 1

        self.vertices_ids[id] = loc


    def add_edge(self, source, dest):
        self.vertices[source][dest] = 1;
        self.vertices[dest][source] = 1

    def remove_vertex(self, id):
        target_index = self.vertices_ids[id]
        last_index = self.size - 1

        print("Removing {}".format(id))

        self.vertices[target_index], self.vertices[last_index] = self.vertices[last_index], self.vertices[target_index]
        print("= = = Testing = = =")
        self.print_graph()
        print("= = = Testing Complete = = =")

        self.vertices.pop()

        for row in self.vertices:
            row[target_index] = row[last_index]
            row.pop()


    def remove_edge(self, source, dest):
        self.vertices[source].adjacent.pop(dest)

    def print_graph(self):
        print("\nPrinting graph - Matrix")
        for row in self.vertices:
            print(row)



if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i, "ID-{}".format(i))
    g.print_graph()
    g.add_edge(0, 1)
    g.print_graph()

    g.add_edge(0, 2)
    g.add_edge(0, 5)

    g.print_graph()

    print(g.vertices_ids)
    g.remove_vertex("ID-3")
    g.print_graph()


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
