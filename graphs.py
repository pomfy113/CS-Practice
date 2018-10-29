"""
A Python program to demonstrate the adjacency
list representation of the graph
"""

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.size = vertices
        self.graph = [None] * self.size

    # Function to add an edge in an directed graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node


    # Function to print the Graph
    def print_graph(self):
        for i in range(self.size):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]

            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")
    # Blech.
    # def depth_search(self, start):
    #     visited = [False] * self.size
    #     visited[start] = True
    #     found = []
    #
    #     node = node.graph[start]
    #
    #     while node is not None:
    #         found.append(node.vertex)
    #         node = node.next

# Driver program to the above graph class
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Printing graph")
    print(g.graph)
    g.print_graph()

    # This code is contributed by Kanav Malhotra
