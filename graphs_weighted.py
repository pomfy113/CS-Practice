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
        # Visited list, along with a stack
        visited = [None] * self.size
        node_stack = []
        nodes = []

        # Initializing
        node = self.nodes[start]
        visited[start] = True
        nodes.append(node.data)

        # Append links to other nodes
        for item in node.adjacent:
            node_stack.append(item)

        # Main while loop; keep popping the stack
        # The stack makes us go deep before exploring the rest
        while len(node_stack) > 0:
            node = node_stack.pop()

            # If not visited, then we put it into the node print
            if visited[node.data] is not True:
                visited[node.data] = True
                for item in node.adjacent:
                    node_stack.append(item)
                nodes.append(node.data)
        print(nodes)

    def depth_first_recursive(self, node, visited=None):
        if visited is None:
            visited = [None] * self.size
            node = self.nodes[node]
            print(node.data)

        visited[node.data] = True
        for node in node.adjacent:
            if visited[node.data] is not True:
                print(node.data)
                self.depth_first_recursive(node, visited)

    def breadth_first(self, start):
        visited = [None] * self.size
        node_stack = deque()
        nodes = []

        node = self.nodes[start]
        visited[start] = True
        nodes.append(node.data)


        for item in node.adjacent:
            node_stack.append(item)

        while len(node_stack) > 0:
            node = node_stack.popleft()

            if visited[node.data] is not True:
                visited[node.data] = True
                for item in node.adjacent:
                    node_stack.append(item)
                nodes.append(node.data)
        print(nodes)
        return nodes

if __name__ == "__main__":
    g = Graph(6)
    g.add_node(0, 1)
    g.add_node(0, 2)
    g.add_node(0, 3)
    g.add_node(0, 4)
    g.add_node(0, 5)

    g.add_node(1, 2)
    g.add_node(2, 0)
    g.add_node(2, 3)
    g.add_node(3, 3)
    g.add_node(3, 4)
    g.add_node(4, 5)

    print(g.nodes)
    g.print_graph()
    print("First, depth first. We should see 2, followed by 3->4->5, then 0->1 since that's left")
    g.depth_first(2)
    print("Then breadth first. We should see 2 which has 0 and 3 since those are immediate adjacents, then go through 1, 4, 5.")
    g.breadth_first(2)
    print("If we start with 0, we go through all of them in order since 0 is adjacent to all")
    g.breadth_first(0)

    g.depth_first_recursive(2)



# test.add_node(0, 1, 1)
# test.add_node(1, 4, 1)
# test.add_node(4, 6, 1)
# test.add_node(3, 6, 2)
# test.add_node(0, 3, 2)
# test.add_node(3, 6, 1)
# test.add_node(0, 6, 4)
