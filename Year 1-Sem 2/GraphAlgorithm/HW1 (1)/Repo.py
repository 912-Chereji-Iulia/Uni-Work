from random import randint

from Graph import Graph


class Repo:
    def __init__(self, file):
        self._file = file
        self._graph = Graph()
        self._load()

    def parse_graph(self):
        return self._graph.parse_graph()

    def add_edge(self, start, end, cost):
        self._graph.add_edge(start, end,cost)

    def nr_of_vertices(self):
        return self._graph.nr_of_vertices()

    def nr_of_edges(self):
        return self._graph.nr_of_edges()

    def valid_vertex(self, vertex):
        return self._graph.valid_vertex(vertex)

    def is_edge(self,start,end):
        return self._graph.is_edge(start, end)

    def add_vertex(self, vertex):
        return self._graph.add_vertex(vertex)

    def get_in_out_degree(self,vertex):
        return self._graph.get_in_out_degree(vertex)

    def delete_vertex(self,vertex):
        return self._graph.delete_vertex(vertex)

    def delete_edge(self,start,end):
        return self._graph.delete_edge(start, end)

    def modify_edge(self,start, end, cost):
        return self._graph.modify_edge(start, end, cost)

    def copy_graph(self):
        return self._graph.copy_graph()

    def parse_in(self, g):
        return self._graph.parse_in(g)

    def parse_out(self, g):
        return self._graph.parse_out(g)

    def get_cost(self, start, end):
        return self._graph.get_cost(start, end)

    def _load(self):
        with open(self._file, "r") as f:
            lines = f.readlines()
            vertex, edges = lines[0].split()
            for i in range(0, int(vertex)):
                self._graph.add_vertex(i)
            list = self.parse_graph()
            for i in range(1, len(lines)):
                x, y, cost = lines[i].split(' ')
                if int(x) not in list:
                    self._graph.add_vertex(int(x))
                if int(y) not in list:
                    self._graph.add_vertex(int(y))
                self.add_edge(int(x), int(y), int(cost))
        f.close()

    def __str__(self):
        return self._graph.__str__()

