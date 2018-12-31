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
                self.vertices[item].pop(vertex)

    def remove_edge(self, source, dest):
        """Removes an edge between source and destination vertex.
        Time: O(1), very straightforward
        """

        if source not in self.vertices:
            raise ValueError("Source vertex not found")
        elif dest not in self.vertices[source]:
            raise ValueError("Destination vertex not found")
        self.vertices[source].pop(dest)

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

    def dijkstra(self, start, search):
        """I can't even say his name right."""
        # Initializing data, along with weights, and already-visited areas
        data = {vtx: float('inf') for vtx in self.vertices}
        queue = [[0, start]]
        visited = set()

        data[start] = 0

        heapq.heapify(queue)

        # We will always visit the lowest TOTAL weight due to it being a
        # priority queue; we will only visit the most worthwhile vertices
        while queue:
            cur_weight, cur_vtx = heapq.heappop(queue)

            # If we haven't visited it yet...
            if cur_vtx not in visited:
                # Let's go through every edge it has
                for edge in self.vertices[cur_vtx]:
                    # Current weight it takes to vertex
                    weight = self.vertices[cur_vtx][edge] + cur_weight

                    # If weight is less, we update it
                    if weight < data[edge]:
                        heapq.heappush(queue, [weight, edge])
                        data[edge] = weight

            # We have now visited this location
            visited.add(cur_vtx)

        # For double checking
        print(data)
        return data[search]

    def bellman_ford(self, start, search):
        # Made into a dictionary to accept more data
        total = {vtx: float('inf') for vtx in self.vertices}
        total[start] = 0

        # We go through the data a "length" amount of times
        for i in range(len(self.vertices)):
            # For every single vtx, we should look at adjacencies
            for vtx in total:
                for adj in self.vertices[vtx]:
                    # We combine what weight we know so far and update the weight...
                    weight = total[vtx] + self.vertices[vtx][adj]
                    # ... but only if we know it's smaller
                    if weight < total[adj]:
                        total[adj] = weight

        # for double checking
        return total[search]


    def prims(self):
        data = {vtx: float('inf') for vtx in self.vertices}
        data[0] = 0
        queue = [(0, 0)]
        visited = set()

        heapq.heapify(queue)

        print(self.vertices)


        while queue:
            print(data)
            print("QUEUE: {}".format(queue))

            weight, vtx = heapq.heappop(queue)
            print("Popped vtx {}, weight {}\n".format(vtx, weight))

            if vtx not in visited:
                visited.add(vtx)
                data[vtx] = weight

                for adj in self.vertices[vtx]:
                    adj_weight = self.vertices[vtx][adj]

                    heapq.heappush(queue, (adj_weight, adj))



        print(data)
        pass

if __name__ == "__main__":
    g = Graph()
    for i in range(7):
        g.add_vertex(i)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 3)
    g.add_edge(0, 4, 7)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 1, 6)
    g.add_edge(2, 3, 11)
    g.add_edge(2, 4, 8)
    g.add_edge(3, 5, 2)
    g.add_edge(4, 3, 2)
    g.add_edge(4, 6, 5)
    g.add_edge(6, 5, 2)
    g.add_edge(6, 3, 10)

    # print(g.dijkstra(0, 5))

    k = Graph()
    for i in range(6):
        k.add_vertex(i)

    k.add_edge(0, 1, 10)
    k.add_edge(0, 5, 8)
    k.add_edge(1, 3, 2)
    k.add_edge(2, 1, 1)
    k.add_edge(3, 2, -2)
    k.add_edge(4, 1, -4)

    k.add_edge(4, 3, -1)
    k.add_edge(5, 4, 1)

    k.bellman_ford(0, 5)
# =========
    h = Graph()
    for i in range(4):
        h.add_vertex(i)
    h.add_edge(0, 1, 10)
    h.add_edge(0, 2, 6)
    h.add_edge(0, 3, 5)
    h.add_edge(1, 3, 15)
    h.add_edge(2, 3, 4)
    h.prims()


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

    # n.prims()
