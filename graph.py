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
        if vertex1 in self.data and vertex2 in self.data and not self.adjacent(vertex1, vertex2):
            self.data[vertex1].append(vertex2)
            self.data[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if self.adjacent(vertex1, vertex2):
            self.data[vertex1].remove(vertex2)
            self.data[vertex2].remove(vertex1)

    def v(self):
        return len(self.data)

    def e(self):
        total = 0
        for vertex in self.data:
            total += len(self.data[vertex])
        return total / 2
