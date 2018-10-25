
class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = {}

class Graph:
    def __init__(self, size):
        self.nodes = [Node(i) for i in range(size)]

    def add_node(self, from_node, to_node, weight):
        self.nodes[from_node].adjacent[to_node] = weight

    def print_graph(self):
        for node in self.nodes:
            print("Current node:", node.data)
            print("Adjacents:", node.adjacent)

            print("\n")


test = Graph(7)
test.add_node(1, 3, 1)
test.add_node(1, 4, 1)
test.add_node(4, 6, 1)
test.add_node(3, 6, 2)
test.add_node(0, 3, 2)
test.add_node(3, 6, 1)
test.add_node(0, 6, 4)


test.print_graph()
