# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# YOUR NAME

import functools

class Graph:

    def __init__(self):
        self.data = dict()

    def adjacent(self, vertex1, vertex2):
        return False

    def neighbors(self, vertex):
        return []

    def add_vertex(self, vertex):
        self.data[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.data:
            del self.data[vertex]

    def add_edge(self, vertex1, vertex2):
        return True
