from collections import deque
import heapq

# This is undirected
class Graph:
    def __init__(self):
        # Key: Node ID, Value: Set() of adjacencies
        self.vertices = {}

    def add_vertex(self, loc):
        """Adds a vertex.
        Time: O(1), Theta is amount of memory a dict is
        """
        self.vertices[loc] = {}

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
            self.vertices[src][dest] = weight
            self.vertices[dest][src] = weight

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

    def prims(self):
        data = {vtx: float('inf') for vtx in self.vertices}
        data[0] = 0
        queue = [(0, 0)]
        visited = set()

        heapq.heapify(queue)

        while queue:
            weight, vtx = heapq.heappop(queue)
            if vtx not in visited:
                visited.add(vtx)

                for adj in self.vertices[vtx]:
                    if adj not in visited:
                        adj_weight = self.vertices[vtx][adj]
                        heapq.heappush(queue, (adj_weight, adj))
                        if data[adj] > adj_weight:
                            data[adj] = adj_weight
        return data

if __name__ == "__main__":
    # g = Graph()
    # for i in range(7):
    #     g.add_vertex(i)
    # g.add_edge(0, 1)
    # g.add_edge(1, 2)
    # g.add_edge(2, 5)
    # g.add_edge(3, 4)
    # # g.add_edge(5, 3)
    # g.add_edge(6, 2)
    #
    #
    # g.print_graph()
    # print(g.cycle_detect())
    #
    # h = Graph()
    # for i in range(4):
    #     h.add_vertex(i)
    # h.add_edge(0, 1, 10)
    # h.add_edge(0, 2, 6)
    # h.add_edge(0, 3, 5)
    # h.add_edge(1, 3, 15)
    # h.add_edge(2, 3, 4)
    #
    # h.prims()

    n = Graph()
    for i in range(9):
        n.add_vertex(i)

    n.add_edge(0, 1, 4)
    n.add_edge(0, 7, 8)
    n.add_edge(1, 7, 11)
    n.add_edge(1, 2, 8)
    n.add_edge(7, 8, 7)
    n.add_edge(7, 6, 1)
    n.add_edge(2, 8, 2)
    n.add_edge(2, 3, 7)
    n.add_edge(2, 5, 4)
    n.add_edge(8, 6, 6)
    n.add_edge(6, 5, 2)
    n.add_edge(3, 5, 14)
    n.add_edge(3, 4, 9)
    n.add_edge(5, 4, 10)

    n.prims()
