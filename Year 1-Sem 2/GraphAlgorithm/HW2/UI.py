from itertools import chain
from random import randint

from Graph import Undirected_Graph


class UI:
    def __init__(self, graph):
        self._graph = graph

    def print_menu(self):
        print("1. Get the nr of vertices")
        print("2. Get the nr of edges")
        print("3. Add an edge")
        print("4. Add a vertex")
        print("5. Edge between 2 vertices")
        print("6. Delete a vertex")
        print("7. Delete an edge")
        print("8. List the graph")
        print("9. Get the connected components")
        print("0.Exit ")

    def start_me(self):

        done = False

        while not done:
            try:
                print('\n')
                self.print_menu()

                cmd = int(input("\nEnter a command>>>"))
                if cmd == 0:
                    print("Bye bye")
                    done = True
                elif cmd == 1:
                    print("The nr of vertices is: " + str(self._graph.nr_of_vertices()))

                elif cmd == 2:
                    print("The nr of edges is: " + str(self._graph.nr_edges()))

                elif cmd == 3:
                    start = int(input("Enter the starting node: "))
                    end = int(input("Enter the ending node: "))
                    if self._graph.valid_vertex(start) == False or self._graph.valid_vertex(end) == False:
                        raise ValueError("The node doesn't exist")
                    if not self._graph.is_edge(start, end):
                        self._graph.add_edge(start, end)
                        print("Added!")
                    else:
                        print("Edge already exists")

                elif cmd == 4:
                    vertex = int(input("Enter a vertex: "))
                    self._graph.add_vertex(vertex)
                    print("Added!")
                elif cmd ==5:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    if self._graph.valid_vertex(vertex1) == True and self._graph.valid_vertex(vertex2) == True:
                        if self._graph.is_edge(vertex1, vertex2):
                            print("There is an edge between these 2 vertices")
                        else:
                            print("There isn't an edge between these 2 vertices")
                    else:
                        raise ValueError("The node doesn't exist")
                elif cmd ==6:
                    vertex = int(input("Enter the vertex to be removed: "))
                    self._graph.delete_vertex(vertex)
                elif cmd == 7:
                    start = int(input("Enter the starting node of the edge to be deleted: "))
                    end = int(input("Enter the ending node of the edge to be deleted: "))
                    self._graph.delete_edge(start, end)

                elif cmd == 8:
                    print("The vertices of the graph are: ")
                    print(self._graph.get_vertices())
                elif cmd==9:
                    self._graph.connected_components()

            except ValueError as ve:
                print(str(ve))







