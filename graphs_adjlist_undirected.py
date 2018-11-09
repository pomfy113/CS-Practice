from collections import deque
import heapq

# This is directed
class Graph:
    def __init__(self):
        # Key: Node ID, Value: Set() of adjacencies
        self.vertices = {}

    def add_vertex(self, loc):
        """Adds a vertex.
        Time: O(1), Theta is amount of memory a dict is
        """
        self.vertices[loc] = []

    def add_edge(self, src, dest, weight=0):
        """Adds an edge, unless it exists or either vertices don't exist.
        Time: O(1), it's constant. We're just adding an item into a set
        Space: O(1), it's just adding a single edge
        """

        if src not in self.vertices:
            raise ValueError("Source vertex not found")
        elif dest not in self.vertices:
            raise ValueError("Destination vertex not found")
        elif dest not in self.vertices[src]:
            self.vertices[src].append(dest)

    def print_graph(self):
        """Prints something.
        Time: O(n), must go through every vertex
        """
        print(self.vertices)


    def find(self, parent, vtx):
        # End of the line
        if parent[vtx] == None:
            return vtx
        else:
            return self.find(parent, parent[vtx])

    def union(self, set, x, y):
        x_parent = self.find(set, x)
        y_parent = self.find(set, y)
        set[x_parent] = y_parent

    def cycle_detect(self):
        """Checks if cycle exists."""
        set = [None] * len(self.vertices)

        for vtx in self.vertices:
            for adj in self.vertices[vtx]:
                vtx_parent = self.find(set, vtx)
                adj_parent = self.find(set, adj)

                if vtx_parent != adj_parent:
                    self.union(set, vtx_parent, adj_parent)
                else:
                    return True

        return False

    def kruskal(self, start, search):
        pass

if __name__ == "__main__":
    g = Graph()
    for i in range(3):
        g.add_vertex(i)
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(2, 1)
    g.print_graph()
    print(g.cycle_detect())
