import heapq
from copy import deepcopy
from random import randint
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self):
        self._dict_in = {}
        self._dict_out = {}
        self._dict_cost = {}
        self.greatest_vertex = -1
        nr_of_vertices = self.nr_of_vertices()
        for i in range(nr_of_vertices):
            self._dict_in[i] = []
            self._dict_out[i] = []

    def nr_of_vertices(self):
        nr_of_vertices = len(self._dict_out.keys())
        return nr_of_vertices

    def nr_of_edges(self):
        nr_of_edges = 0
        for i in self._dict_out.keys():
            nr_of_edges = nr_of_edges + len(self._dict_out[i])
        return nr_of_edges

    def add_edge(self, start, end, cost):
        self._dict_out[start].append(end)
        self._dict_in[end].append(start)
        self._dict_cost[(start, end)] = cost

    def is_edge(self, start, end):
        if start not in self._dict_out:
            raise ValueError("The start vertex doesn't exist")
        if end in self._dict_out[start]:
            return True
        return False

    def copy_graph(self):
        return deepcopy(self)

    def add_vertex(self, vertex):
        if vertex in self._dict_out.keys():
            raise ValueError("This vertex already exists")
        self._dict_out[vertex] = []
        self._dict_in[vertex] = []

    def delete_vertex(self, vertex):
        if vertex not in self._dict_out.keys():
            raise ValueError("Invalid vertex")
        nr_edges = self.nr_of_edges()
        for element in self._dict_out[vertex]:
            self._dict_cost.pop(vertex, element)
            self._dict_in[element].remove(vertex)
            nr_edges -= 1

        for element in self._dict_in[vertex]:
            self._dict_cost.pop(element,vertex)
            self._dict_out[element].remove(vertex)
            nr_edges -= 1

        self._dict_in.pop(vertex)
        self._dict_out.pop(vertex)
        nr_edges -= 1

    def delete_edge(self,start, end):
        if not self.is_edge(start, end) :
            raise ValueError("There isn't an edge between these 2.")

        self._dict_out[start].remove(end)
        self._dict_in[end].remove(start)
        self._dict_cost.pop((start, end))
        nr_edges = self.nr_of_edges()
        nr_edges -= 1

    def modify_edge(self, start, end, new_cost):
        if not self.is_edge(start, end) :
            raise ValueError("Error modifying the provided edge")
        edge = (start, end)
        self._dict_cost[edge] = new_cost

    def get_in_out_degree(self, vertex):
        if vertex not in self._dict_out:
            raise ValueError("The vertex doesn't exist")
        in_degree = len(self._dict_in[vertex])
        out_degree = len(self._dict_out[vertex])
        return in_degree, out_degree

    def valid_vertex(self, vertex):
        if vertex not in self._dict_out.keys() and vertex not in self._dict_in.keys():
            return False
        return True

    def parse_out(self, v):
        return self._dict_out[v]

    def parse_in(self, v):
        return self._dict_in[v]

    def parse_edges(self):
        return list(self._dict_cost.items())

    def parse_graph(self):
        return self._dict_out.keys()

    def get_cost(self, start, end):
        if not self.is_edge(start, end):
            raise ValueError("This edge doesn't exist")
        edge = (start, end)
        return self._dict_cost[edge]

    def lowest_cost_walk_with_backward_Dijkstra(self, v1, v2):
        distance = {}
        distance[v2] = 0

        priority_queue = []
        heapify(priority_queue)
        heapq.heappush(priority_queue, (0, v2))

        visited = []
        next = {}
        next[v2] = v2

        while len(priority_queue) > 0:
            x = heappop(priority_queue)[1]
            if x in visited:
                continue
            visited.append(x)
            for y in self.parse_in(x):
                if self.get_cost(y, x) < 0:
                    raise Exception("We can't have negative costs")
                if y not in distance or distance[y] > distance[x] + self.get_cost(y, x):
                    distance[y] = distance[x] + self.get_cost(y, x)
                    next[y] = x
                    heappush(priority_queue, (distance[y], y))

        if v1 not in visited:
            raise Exception("Walk was not found")

        path = []
        node = v1
        while next[node] != node:
            path.append(node)
            node = next[node]
        path.append(v2)
        return distance[v1], path

    def __str__(self):
        string = ''
        for i in self._dict_out.keys():
            for j in self._dict_out[i]:
                string += str(i) + " " + str(j) + ' '+ str(self._dict_cost[(i, j)])+'\n'
        return string


def generate_a_random_graph(nr_vertices, nr_edges):
    random = Graph()
    if nr_vertices*nr_vertices < nr_edges:
        nr_edges = nr_vertices*nr_vertices
    for i in range(nr_vertices):
        random.add_vertex(i)
    i=0
    while i < nr_edges:
        start = randint(0, nr_vertices-1)
        end = randint(0, nr_vertices - 1)
        cost = randint(0,100)
        if not random.is_edge(start, end):
            random.add_edge(start, end, cost)
            i=i+1
    return random

