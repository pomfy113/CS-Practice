from collections import deque

# This is directed
class Graph:
    def __init__(self):
        # Key: Node ID, Value: Set() of adjacencies
        self.vertices = {}

    def add_vertex(self, loc):
        """Adds a vertex.
        Time: O(1), Theta is amount of memory a set is
        """
        self.vertices[loc] = set()

    def add_edge(self, src, dest):
        """Adds an edge, unless it exists or either vertices don't exist.
        Time: O(1), it's constant. We're just adding an item into a set
        Space: O(1), it's just adding a single edge
        """

        if src not in self.vertices:
            raise ValueError("Source vertex not found")
        elif dest not in self.vertices:
            raise ValueError("Destination vertex not found")
        elif dest not in self.vertices[src]:
            self.vertices[src].add(dest)

    def remove_vertex(self, vertex):
        """Removes a vertex and associated adjacencies.
        Time: O(n), going to have to go through EVERY vertex to remove adjacencies
            to previously deleted vertex.
        """
        if vertex not in self.vertices:
            raise ValueError("Vertex not found")

        self.vertices.pop(vertex)

        # Remoing related adjacencies
        for item in self.vertices:
            if vertex in self.vertices[item]:
                self.vertices[item].remove(vertex)

    def remove_edge(self, source, dest):
        """Removes an edge between source and destination vertex.
        Time: O(1), very straightforward
        """

        if source not in self.vertices:
            raise ValueError("Source vertex not found")
        elif dest not in self.vertices[source]:
            raise ValueError("Destination vertex not found")
        self.vertices[source].remove(dest)

    def print_graph(self):
        """Prints something.
        Time: O(n), must go through every vertex
        """
        print(self.vertices)

    def dfs(self, start, search):
        """Searches for item iteratively, depth first style.
        Space: O(n); best case, none, worst case 2n
            Best: We land right on top of the search. Um.
            Worst: case involves having a place with only neighbors.
                The stack is going to have all said neighbors before going down
        Time: O(n), usually; best case is immediate, worst case is n.
            Worst, if it's the final neighbor, OR, if it's something in order
                1 -> 2 -> 3 -> 4, looking for 4.
            Best is landing on it. Barring that, it's the first neighbor we hit.
        """
        if start == search:
            return True
        # Initialization
        visited = set([start])
        search_stack = []
        search_stack.append(start)

        # Keeps going down stack; prioritizes adjacencies
        while len(search_stack) > 0:
            # Keep popping; go down adjacencies
            next = search_stack.pop()
            visited.add(next)
            # End case
            if next == search:
                return True
            else:
                # Else, look for all adjecencies and put into stack
                for adj in self.vertices[next]:
                    if adj not in visited:
                        search_stack.append(adj)
        return False

    def dfs_recursive(self, vertex, search, visited=None):
        """Searches for item recursively, depth first style.
            Big O is mostly same as the other dfs, but with slightly different
            ordering due to how a stack works.
            Mostly.
            We need more space due to passing down the 'visited' each time. It is
            cleaner, sure, but at what cost?
        """
        # Init
        if visited is None:
            visited = set([vertex])

        visited.add(vertex)

        # End condition; item found
        if vertex == search:
            return True

        # Otherwise, keep going down the children
        for adj in self.vertices[vertex]:
            if adj not in visited:
                found = self.dfs_recursive(adj, search, visited)
                # Needed if we found it
                if found is True:
                    return True
        # Final case; if not found, return false
        return False

    def bfs(self, start, search):
        """Searches for item iteratively, breadth first style.
            Same as dfs. Without the deque, time would take a hit due to how
            the list inherently works, but deque() should make it constant.
        """
        # Init; queue instead of stack
        visited = set([start])
        search_queue = deque()
        search_queue.append(start)

        # Keep popping out from queue; prioritizes neighbors
        while len(search_queue) > 0:
            next = search_queue.popleft()
            visited.add(next)
            # End case; item found
            if next == search:
                return True
            else:
                # Else, we go through adjacencies
                for adj in self.vertices[next]:
                    if adj not in visited:
                        search_queue.append(adj)
        return False

    def cycle_detect(self):
        """Checks if cycle exists.
            See above, but now we have to do it n times.
            Time: O(n^2) max, if we have to go through every single vertex.
                We CAN optimize it if we know specific things about what we're
                passing in, like say, if EVERYTHING is connected.
                However, we do not know this. Better safe than sorry.
            Space: Same as above; we overwrite them each time we go down the for
                loop, so there should be no issues.
        """
        # We want to go through ALL of them, even if not connected
        for vtx in self.vertices:
            visited = set([])
            search_stack = []
            search_stack.append(vtx)

            # Keep going down the stack
            while len(search_stack) > 0:
                index = search_stack.pop()
                # If we find our origin again, we found a loop
                if vtx in visited:
                    return True
                else:
                    # Keep going down the vertices
                    for adj in self.vertices[index]:
                        if adj not in visited:
                            visited.add(adj)
                            search_stack.append(adj)
        return False


# if __name__ == "__main__":
#     g = Graph()
#     for i in range(7):
#         g.add_vertex(i)
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(0, 3)
#     g.add_edge(0, 4)
#     g.add_edge(0, 5)
#
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#     g.add_edge(2, 3)
#     g.add_edge(3, 3)
#     g.add_edge(3, 4)
#     g.add_edge(4, 5)
#     g.print_graph()
#
#     print("Starting dfs")
#     g.dfs(2, 3)
#     print("= = = Starting recursive, should return= = = ")
#     g.dfs_recursive(2, 3)
#     print("= = = Continuing recursive, should be false= = = ")
#     g.dfs_recursive(2, 6)
#     print("= = = Starting bfs = = = ")
#
#     g.bfs(2, 3)
#     print("Cycle detection")
#     g.cycle_detect()
#
#     print("Let's try a different once")
#     h = Graph()
#     for i in range(8):
#         h.add_vertex(i)
#     h.add_edge(0, 1)
#     h.add_edge(0, 2)
#     h.add_edge(0, 3)
#     h.add_edge(0, 4)
#     h.add_edge(2, 4)
#     h.add_edge(3, 4)
#     h.add_edge(4, 5)
#     # Should not have a cycle
#     print(h.cycle_detect())
#
#     h.add_edge(6, 7)
#     h.add_edge(7, 6)
#
#     # Should have a cycle
#     print(h.cycle_detect())




# test.add_edge(0, 1, 1)
# test.add_edge(1, 4, 1)
# test.add_edge(4, 6, 1)
# test.add_edge(3, 6, 2)
# test.add_edge(0, 3, 2)
# test.add_edge(3, 6, 1)
# test.add_edge(0, 6, 4)
