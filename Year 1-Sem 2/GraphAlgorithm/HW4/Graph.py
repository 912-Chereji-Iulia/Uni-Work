from copy import deepcopy
from queue import Queue
from random import randint


class Graph:
    def __init__(self):
        self._dict_in = {}
        self._dict_out = {}
        self._dict_cost = {}
        self._duration={}
        nr_of_vertices = self.nr_of_vertices()
        for i in range(nr_of_vertices):
            self._dict_in[i] = []
            self._dict_out[i] = []


    def get_duration(self,x):
        return self._duration[x]

    def add_vertex_duration(self,x, d):
        self._duration[x]=d

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
        return [in_degree, out_degree]

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

    # we take a vertex with no predecessors, we put it on the sorted list, and we eliminate it from the graph.
    # Then, we take a vertex with no predecessors from the remaining graph and continue the same way.
    # not actually remove vertices, but to keep, for each vertex, a counter of predecessors still in the graph
    def predecessor_counting_alg(self, sorted_list):
        q = Queue()
        count = {}
        for x in self.parse_graph():
            count[x], y1 = self.get_in_out_degree(x)
            if count[x] == 0:
                q.put(x)
        while not q.empty():
            x = q.get()
            sorted_list.append(x)
            for y in self.parse_out(x):
                count[y] = count[y]-1
                if count[y] == 0:
                    q.put(y)
        if len(sorted_list) < len(self.parse_graph()):
            return False
        return True

    def compute_earliest_times(self, sorted_list, early_start, early_end):
        for i in sorted_list:
            maxim = 0
            ok = 1
            for x in self.parse_in(i):
                if maxim < early_end[x] or maxim == early_end[x] == 0:
                    maxim = early_end[x]
                    ok = 0
            early_start[i] = maxim
            if ok == 1:
                early_end[i] = early_start[i]
            else:
                early_end[i] = early_start[i] + self.get_duration(i)

    def compute_latest_times(self, sorted_list, late_start, late_end):
        for i in range(len(sorted_list)-2, -1, -1):
            minim = 999999
            ok = 1
            for x in self.parse_out(sorted_list[i]):
                if minim > late_start[x]:
                    minim = late_start[x]
                    ok = 0
            late_end[sorted_list[i]] = minim
            if ok == 1:
                late_start[sorted_list[i]] = late_end[sorted_list[i]]
            else:
                late_start[sorted_list[i]] = late_end[sorted_list[i]] - self.get_duration(sorted_list[i])

    def critical_activities(self):
        sorted_list = []
        if self.predecessor_counting_alg(sorted_list) is False:
            print("This is not a DAG")
            return

        print("Topological sorting order: ")
        for i in sorted_list:
            print(i, end=" ")
        print("\n")

        earliest_start = {}
        earliest_end = {}
        latest_start = {}
        latest_end = {}
        for i in self.parse_graph():
            earliest_start[i] = 0
            earliest_end[i] = 0
            latest_start[i] = 0
            latest_end[i] = 0

        self.compute_earliest_times(sorted_list, earliest_start, earliest_end)
        latest_start['Y'] = earliest_end['Y']
        latest_end['Y'] = earliest_end['Y']
        self.compute_latest_times(sorted_list, latest_start, latest_end)

        print("ACTIVITY              earliest start time              earliest end time              latest start time              latest end time")
        for i in sorted_list:
            print( i + "                      " + str(earliest_start[i]), end="")
            print("                                 " + str(earliest_end[i]), end="")
            print("                               " + str(latest_start[i]), end="")
            print("                               " + str(latest_end[i]), end="\n")

        print("The total time of the project: " + str(latest_end['Y']))

        critical = []
        for i in sorted_list:
            if earliest_end[i] == latest_end[i]:# critical activities => latest_end = earliest_end
                critical.append(i)
        print("Critical activities are: ", end=" ")
        for i in critical:
            print(i, end=" ")
        print("\n")



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
    while(i < nr_edges):
        start = randint(0, nr_vertices-1)
        end = randint(0, nr_vertices - 1)
        cost = randint(0,100)
        if not random.is_edge(start, end):
            random.add_edge(start, end, cost)
            i=i+1
    return random

