from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = {}
    def __repr__(self):
        return '<Node {}>'.format(self.data)
    def __str__(self):
        return '<Node {}>'.format(self.data)

class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = [Node(i) for i in range(size)]

    # Assume 1 weight
    def add_node(self, from_node, to_node, weight=1):
        next_node = self.nodes[to_node]
        self.nodes[from_node].adjacent[next_node] = weight

    def print_graph(self):
        for node in self.nodes:
            print("Current node:", node.data)
            print("Adjacents:", node.adjacent)

            print("\n")

    def depth_first(self, start):
        visited = [None] * self.size
        visited[start] = True
        node_stack = deque()

        node = self.nodes[start]
        print(node.data)
        for item in node.adjacent:
            node_stack.append(item)

        while len(node_stack) > 0:
            node = node_stack.pop()

            if visited[node.data] is not True:
                visited[node.data] = True
                for item in node.adjacent:
                    node_stack.append(item)
                print(node.data)

if __name__ == "__main__":
    g = Graph(6)
    g.add_node(0, 1)
    g.add_node(0, 2)
    g.add_node(1, 2)
    g.add_node(2, 0)
    g.add_node(2, 3)
    g.add_node(3, 3)
    g.add_node(3, 4)
    g.add_node(4, 5)

    print(g.nodes)
    g.print_graph()
    g.depth_first(0)

# test.add_node(0, 1, 1)
# test.add_node(1, 4, 1)
# test.add_node(4, 6, 1)
# test.add_node(3, 6, 2)
# test.add_node(0, 3, 2)
# test.add_node(3, 6, 1)
# test.add_node(0, 6, 4)
