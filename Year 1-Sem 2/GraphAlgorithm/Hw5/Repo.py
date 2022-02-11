from random import randint

from Graph import Undirected_Graph


class Repo:
    def __init__(self, file):
        self._file = file
        self._graph = Undirected_Graph()
        self._load()

    def parse_graph(self):
        return self._graph.parse_graph()

    def add_edge(self, start, end):
        self._graph.add_edge(start, end)

    def nr_of_vertices(self):
        return self._graph.nr_of_vertices()

    def nr_edges(self):
        return self._graph.nr_edges()

    def valid_vertex(self, vertex):
        return self._graph.is_vertex(vertex)

    def is_edge(self,start,end):
        return self._graph.is_edge(start, end)

    def add_vertex(self, vertex):
        return self._graph.add_vertex(vertex)

    def delete_vertex(self,vertex):
        return self._graph.delete_vertex(vertex)

    def delete_edge(self,start,end):
        return self._graph.delete_edge(start, end)

    def get_vertices(self):
        return self._graph.get_vertices()

    def get_edges(self):
        return self._graph.edges

    def _load(self):
        f = open(self._file, 'rt')

        list_vertices = []
        for i in f.readline().split(' '):
            list_vertices.append(int(i))
        nr_vertices = int(list_vertices[0])
        for i in range(0, nr_vertices):
            self.add_vertex(i)

        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.split(' ')
            start = int(line[0])
            end = int(line[1])

            self.add_edge(start, end)

    def connected_components(self):
        return self._graph.connected_components()

    def vertex_cover(self):
        return self._graph.cover_vertex()

    def vertex_cover_2(self):
        return self._graph.cover_vertex_2()

    def __str__(self):
        return self._graph.__str__()

