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


    def find(self, set, vtx):
        """Find the end of the line."""
        # If it doesn't have children OR we loop back to the same vtx
        if set[vtx] == None:
            return vtx
        # Keep going down the line
        else:
            return self.find(set, set[vtx])

    def union(self, set, x, y):
        """Creates a union."""
        x_end = self.find(set, x)
        y_end = self.find(set, y)
        # End of y becomes end of x
        set[x_end] = y_end

    def cycle_detect(self):
        """Checks if cycle exists."""
        set = {vtx: None for vtx in self.vertices}

        # Let's go through every vertex and their partner
        for vtx in self.vertices:
            for next in self.vertices[vtx]:
                vtx_end = self.find(set, vtx)
                next_end = self.find(set, next)

                # If they don't end
                if vtx_end != next_end:
                    self.union(set, vtx_end, next_end)
                else:
                    return True

        return False

    def kruskal(self, start, search):
        pass

if __name__ == "__main__":
    g = Graph()
    for i in range(7):
        g.add_vertex(i)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    # g.add_edge(5, 3)
    g.add_edge(6, 2)


    g.print_graph()
    print(g.cycle_detect())
