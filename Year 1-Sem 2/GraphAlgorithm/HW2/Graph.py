from copy import deepcopy
from random import randint, random


class Undirected_Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.cost={}

    def nr_of_vertices(self):
        nr_of_vertices = len(self.vertices.keys())
        return nr_of_vertices

    def nr_edges(self):
        return len(self.edges)

    def is_edge(self, start, end):
        if (start, end) in self.edges or (end, start) in self.edges:
            return True
        return False

    def is_vertex(self, v):
        if v in self.vertices.keys():
            return True
        return False

    def add_edge(self, start, end):
        if self.is_vertex(start) is False or self.is_vertex(end) is False:
            print("Invalid vertices")
        if self.is_edge(start, end):
            print("Edge already exists")
        else:
            self.edges.append((start, end))
            self.vertices[end].append(start)
            self.vertices[start].append(end)

    def parse_graph(self):
        a = self.get_vertices()
        line = ""
        for i in a:
            line = line + str(i) + " "


    def copy_graph(self):
        graph = Undirected_Graph()
        graph.edges = self.edges
        graph.vertices = self.vertices
        return graph

    def add_vertex(self, v):
        if self.is_vertex(v):
            print("Vertex already exist")
        else:
            self.vertices[v] = []

    def delete_edge(self, v1, v2):
        if self.is_edge(v1, v2) is False:
            print("The edge does not exist!")
        else:
            for i in self.vertices[v2]:
                if i == v1:
                    self.vertices[v2].remove(i)
            for i in self.vertices[v1]:
                if i == v2:
                    self.vertices[v1].remove(i)
            if (v1, v2) in self.edges:
                self.edges.remove((v1, v2))
            elif (v2, v1) in self.edges:
                self.edges.remove((v2, v1))

    def delete_vertex(self, v):
        if self.is_vertex(v) is False:
            print("The vertex does not exist!")
        else:
            for i in self.vertices[v]:
                if (i, v) in self.edges:
                    self.edges.remove((i, v))
                elif (v, i) in self.edges:
                    self.edges.remove((v, i))
                self.vertices[i].remove(v)
            del self.vertices[v]

    def con_comp(self, v, e):
        new_graph = Undirected_Graph()
        new_graph.vertices = deepcopy(v)
        new_graph.edges = deepcopy(e)
        return new_graph

    def get_vertices(self):
        vertices = []
        for i in self.vertices.keys():
            vertices.append(i)
        return vertices

    def accessible_DFS(self, res, v, visited):
        '''

        :param res: the resulted list of accessible vertices
        :param v: the current vertex
        :param visited: list of visited vertices
        :return:
        '''

        visited[v] = True   # Mark the current vertex as visited
        res.append(v)
        # Add all vertices adjacent to v to the result list
        for i in self.vertices[v]:
            if not visited[i]:
                res = self.accessible_DFS(res, i, visited)
        return res

    def connected_components(self):
        visited = {}
        for i in range(self.nr_of_vertices()+1):
            visited[i]=True
            if i in self.vertices.keys():
                visited[i] = False

        connected_comp = []
        for vertex in range(self.nr_of_vertices()+1):
            if not visited[vertex]:
                res = []
                list_accessible = self.accessible_DFS(res, vertex, visited)
                edges_connected_comp = []
                for i in list_accessible:
                    for j in list_accessible:
                        if self.is_edge(i, j):
                            if (i, j) not in edges_connected_comp and (j, i) not in edges_connected_comp:
                                edges_connected_comp.append((i, j))
                if len(edges_connected_comp) == 0:
                     print("Connected component-isolated point: " + str(list_accessible) )
                else:
                     print("Connected component: " + str(list_accessible) + " with edges: " + str(edges_connected_comp))
                new_con_comp = self.con_comp(list_accessible, edges_connected_comp)
                connected_comp.append(new_con_comp)

        return connected_comp


