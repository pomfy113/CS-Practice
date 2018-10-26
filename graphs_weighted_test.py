#!python
from graphs_weighted import Graph, Node
from collections import Set
import unittest


class RecursionTest(unittest.TestCase):
    def test_basic_graph_functions(self):
        g = Graph(4)
        g.add_node(0, 1)
        g.add_node(0, 2)
        assert len(g.nodes) == 4
        assert len(g.nodes[0].adjacent) == 2

    def test_adjacency(self):
        g = Graph(6)

        """
        * * *  Adjacency Test: Node 0 * * *
        Basic adjacency
        """
        should_be_adjacent_to_0 = [1, 2]
        is_adjacent_to_0 = []

        for i in should_be_adjacent_to_0:
            g.add_node(0, i)
        for item in g.nodes[0].adjacent:
            is_adjacent_to_0.append(item.data)

        assert should_be_adjacent_to_0 == is_adjacent_to_0

        # Let's try another append
        should_be_adjacent_to_0.append(5)
        g.add_node(0, 5)

        is_adjacent_to_0 = []
        for item in g.nodes[0].adjacent:
            is_adjacent_to_0.append(item.data)

        assert should_be_adjacent_to_0 == is_adjacent_to_0

        """
        * * *  Adjacency Test: Node 1 * * *
        More of the same, but let's test to make sure nothing else gets affected
        """
        should_be_adjacent_to_1 = [0, 1, 3]
        is_adjacent_to_1 = []

        for i in should_be_adjacent_to_1:
            g.add_node(1, i)
        for item in g.nodes[1].adjacent:
            is_adjacent_to_1.append(item.data)

        # Make sure 0 is unaffected
        assert should_be_adjacent_to_0 == is_adjacent_to_0
        assert should_be_adjacent_to_1 == is_adjacent_to_1

        """
        * * * Adjacency Test: Node 2 * * *
        Let's go for an empty
        """
        should_be_adjacent_to_2 = []
        is_adjacent_to_2 = []

        ## Make sure 0 is unaffected
        assert should_be_adjacent_to_2 == is_adjacent_to_2

if __name__ == '__main__':
    unittest.main()
