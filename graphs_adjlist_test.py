#!python
from graphs_adjlist import Graph
import unittest

# Note - this is a directed graph
class RecursionTest(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        g.add_vertex(1)
        assert len(g.vertices) == 1
        assert 1 in g.vertices
        assert g.vertices[1] == set([])

        g.add_vertex(2)
        assert len(g.vertices) == 2
        assert 2 in g.vertices

        g.add_vertex(1)
        assert len(g.vertices) == 2
        assert 1 in g.vertices
        assert g.vertices[1] == set([])

    def test_adjacency(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)

        # Edge should exist only in 1
        g.add_edge(1, 2)
        assert 2 in g.vertices[1]
        assert 1 not in g.vertices[2]

        # Edge should exist only in 1
        g.add_edge(2, 1)
        assert 2 in g.vertices[1]
        assert 1 in g.vertices[2]

        # 4 does not exist yet; should throw error
        with self.assertRaises(ValueError):
            g.add_edge(1, 4)
        assert 2 in g.vertices[1]
        assert 4 not in g.vertices[1]

        # Let's try a nonexistent source
        with self.assertRaises(ValueError):
            g.add_edge(5, 4)

        # Vtx 1 should now have an extra one
        g.add_vertex(3)
        g.add_edge(1,3)
        assert 2 in g.vertices[1]
        assert 3 in g.vertices[1]

    def test_remove(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1, 2)
        g.add_edge(1, 3)

        # Should be removed
        g.remove_edge(1, 2)
        assert 2 not in g.vertices[1]
        assert 3 in g.vertices[1]

        assert 1 not in g.vertices[2]
        assert 3 not in g.vertices[2]

        assert 1 not in g.vertices[3]
        assert 2 not in g.vertices[3]

        # Let's reset that and add more things that link to 3
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        assert 3 in g.vertices[1]
        assert 3 in g.vertices[2]

        # And remove 3
        g.remove_vertex(3)

        # It should stop existing, even in previous adjacincies
        assert 3 not in g.vertices[1]
        assert 3 not in g.vertices[2]
        assert 3 not in g.vertices

        # Delete something that doesn't exist,
        with self.assertRaises(ValueError):
            g.remove_vertex(6)

        # Let's make 1 not exist
        g.remove_vertex(1)

        with self.assertRaises(ValueError):
            g.add_edge(2, 1)

        assert 1 not in g.vertices

        # Adding edges
        with self.assertRaises(ValueError):
            g.add_edge(2, 1)
        with self.assertRaises(ValueError):
            g.add_edge(1, 2)
        # Removing edges that can't exist, src and dest
        with self.assertRaises(ValueError):
            g.remove_edge(5, 6)
        with self.assertRaises(ValueError):
            g.remove_edge(1, 6)

    def test_dfs(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1,2)

        # We should only have 1 to 2 due to it being directed
        assert g.dfs(1, 1) is True
        assert g.dfs(1, 2) is True
        assert g.dfs(1, 3) is False
        assert g.dfs(2, 1) is False
        assert g.dfs(2, 2) is True
        assert g.dfs(2, 3) is False
        assert g.dfs(3, 1) is False
        assert g.dfs(3, 2) is False
        assert g.dfs(3, 3) is True


        g.add_edge(3, 1)
        # Copy of previous, save for 3 to 1, which leads to 2 as well
        assert g.dfs(1, 1) is True
        assert g.dfs(1, 2) is True
        assert g.dfs(1, 3) is False
        assert g.dfs(2, 1) is False
        assert g.dfs(2, 2) is True
        assert g.dfs(2, 3) is False
        assert g.dfs(3, 1) is True
        assert g.dfs(3, 2) is True
        assert g.dfs(3, 3) is True


    def test_dfs_recursive(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1,2)

        # We should only have 1 to 2 due to it being directed
        assert g.dfs_recursive(1, 1) is True
        assert g.dfs_recursive(1, 2) is True
        assert g.dfs_recursive(1, 3) is False
        assert g.dfs_recursive(2, 1) is False
        assert g.dfs_recursive(2, 2) is True
        assert g.dfs_recursive(2, 3) is False
        assert g.dfs_recursive(3, 1) is False
        assert g.dfs_recursive(3, 2) is False
        assert g.dfs_recursive(3, 3) is True


        g.add_edge(3, 1)
        # Copy of previous, save for 3 to 1, which leads to 2 as well
        assert g.dfs_recursive(1, 1) is True
        assert g.dfs_recursive(1, 2) is True
        assert g.dfs_recursive(1, 3) is False
        assert g.dfs_recursive(2, 1) is False
        assert g.dfs_recursive(2, 2) is True
        assert g.dfs_recursive(2, 3) is False
        assert g.dfs_recursive(3, 1) is True
        assert g.dfs_recursive(3, 2) is True
        assert g.dfs_recursive(3, 3) is True


    def test_bfs(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_edge(1,2)

        # We should only have 1 to 2 due to it being directed
        assert g.bfs(1, 1) is True
        assert g.bfs(1, 2) is True
        assert g.bfs(1, 3) is False
        assert g.bfs(2, 1) is False
        assert g.bfs(2, 2) is True
        assert g.bfs(2, 3) is False
        assert g.bfs(3, 1) is False
        assert g.bfs(3, 2) is False
        assert g.bfs(3, 3) is True


        g.add_edge(3, 1)
        # Copy of previous, save for 3 to 1, which leads to 2 as well
        assert g.bfs(1, 1) is True
        assert g.bfs(1, 2) is True
        assert g.bfs(1, 3) is False
        assert g.bfs(2, 1) is False
        assert g.bfs(2, 2) is True
        assert g.bfs(2, 3) is False
        assert g.bfs(3, 1) is True
        assert g.bfs(3, 2) is True
        assert g.bfs(3, 3) is True

    def test_cyclic_detection(self):
        g = Graph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_vertex(4)


        assert g.cycle_detect() is False

        # Let's add a straight line
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        assert g.cycle_detect() is False

        # move from 3 to 1
        g.add_edge(3, 1)
        assert g.cycle_detect() is True
        g.remove_edge(3, 1)

        # Looping 4 to 4
        g.add_edge(4, 4)
        assert g.cycle_detect() is True
        # Removed 4 to 4
        g.remove_edge(4, 4)
        assert g.cycle_detect() is False

if __name__ == '__main__':
    unittest.main()
