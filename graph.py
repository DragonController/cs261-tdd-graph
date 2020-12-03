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
        if vertex1 in self.data:
            for neighbor in self.data[vertex1]:
                if vertex2 == neighbor:
                    return True
        return False

    def neighbors(self, vertex):
        if vertex in self.data:
            return self.data[vertex]
        return []

    def add_vertex(self, vertex):
        if not vertex in self.data:
            self.data[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.data:
            for neighbor in self.neighbors(vertex):
                self.data[neighbor].remove(vertex)
            del self.data[vertex]

    def add_edge(self, vertex1, vertex2):
        return True

    def remove_edge(self, vertex1, vertex2):
        return True
