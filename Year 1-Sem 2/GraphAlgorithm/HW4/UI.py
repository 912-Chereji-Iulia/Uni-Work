
from random import randint

from Graph import Graph, generate_a_random_graph


class UI:
    def __init__(self, graph):
        self._graph = graph

    def print_menu(self):
        print("1. Get the nr of vertices")
        print("2. Get the nr of edges")
        print("3. Add an edge")
        print("4. Add a vertex")
        print("5. Get the in degree and the out degree of a specified vertex")
        print("6. Create a random graph")
        print("7. Edge between 2 vertices")
        print("8. Delete a vertex")
        print("9. Delete an edge")
        print("10. List the graph")
        print("11. Modify the cost of an edge")
        print("12. Parse the set of inbound edges of a specified vertex ")
        print("13. Parse the set of outbound edges of a specified vertex ")
        print("14. Copy the graph")
        print("15. Parse the graph")
        print("16. Get the cost of an edge")
        print("17. Activities")
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
                elif cmd == 10:
                    print(self._graph)
                elif cmd == 1:
                    print("The nr of vertices is: " + str(self._graph.nr_of_vertices()))

                elif cmd == 2:
                    print("The nr of edges is: " + str(self._graph.nr_of_edges()))

                elif cmd == 3:
                    start = int(input("Enter the starting node: "))
                    end = int(input("Enter the ending node: "))
                    cost = int(input("Enter the cost: "))
                    if self._graph.valid_vertex(start) == False or self._graph.valid_vertex(end) == False:
                        raise ValueError("The node doesn't exist")
                    if not self._graph.is_edge(start, end):
                        self._graph.add_edge(start, end, cost)
                        print("Added!")
                    else:
                        print("Edge already exists")

                elif cmd == 4:
                    vertex = int(input("Enter a vertex: "))
                    self._graph.add_vertex(vertex)
                    print("Added!")
                elif cmd == 5:
                    vertex = int(input("Enter a vertex: "))
                    in_d, out_d = self._graph.get_in_out_degree(vertex)
                    print("The in degree is: " + str(in_d) + " and the out degree is: " + str(out_d))
                elif cmd == 6:
                    nr_vertices = int(input("Select the number of vertexes: "))
                    nr_edges = int(input("Select the number of edges: "))
                    g = generate_a_random_graph(nr_vertices, nr_edges)
                    if nr_vertices*nr_vertices < nr_edges:
                        print("We cannot obtain a graph with that many edges. The maximum nr of edges is nr_vertices * nr_vertices  ")
                    file_save = input("Save the file: ")
                    list = g.parse_graph()

                    with open(file_save, "w+") as f:
                        f.write(str(g.nr_of_vertices()) + ' ' + str(g.nr_of_edges()) + "\n")
                        for i in list:
                            for j in g.parse_out(i):
                                cost = g.get_cost(i, j)
                                f.write(str(i) + ' ' + str(j) + ' ' + str(cost) + "\n")
                    f.close()
                elif cmd == 7:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    if self._graph.valid_vertex(vertex1) == True and self._graph.valid_vertex(vertex2) == True:
                        if self._graph.is_edge(vertex1, vertex2):
                            print("There is an edge between these 2 vertices")
                        else:
                            print("There isn't an edge between these 2 vertices")
                    else:
                        raise ValueError("The node doesn't exist")
                elif cmd == 8:
                    vertex = int(input("Enter the vertex to be removed: "))
                    self._graph.delete_vertex(vertex)
                elif cmd == 9:
                    start = int(input("Enter the starting node of the edge to be deleted: "))
                    end = int(input("Enter the ending node of the edge to be deleted: "))
                    self._graph.delete_edge(start, end)
                elif cmd == 11:
                    start = int(input("Enter the starting node of the edge to be updated: "))
                    end = int(input("Enter the ending node of the edge to be updated: "))
                    cost = int(input("Enter the new cost: "))
                    self._graph.modify_edge(start, end, cost)
                elif cmd==12:
                    vertex=int(input("Enter a vertex: "))

                    set = self._graph.parse_in(vertex)
                    if len(set)!=0:
                        print("The set of inbound neighbours of " + str(vertex) + " is: ")
                        for i in set:
                            print(' ' + str(i), end='')
                        print('\n')
                    else:
                        print(str(vertex)+ " doesn't have inbound neighbours")
                elif cmd==13:
                    vertex = int(input("Enter a vertex: "))

                    set=self._graph.parse_out(vertex)
                    if len(set) != 0:
                        print("The set of outbound neighbours of " + str(vertex) + " is: ")
                        for i in set:
                            print(' ' + str(i), end='')
                        print('\n')
                    else:
                        print(str(vertex) + " doesn't have outbound neighbours")
                elif cmd==14:
                    copy=self._graph.copy_graph()
                    print(copy)
                elif cmd == 15:
                    set1 = self._graph.parse_graph()
                    print("The vertices of the graph are: ")
                    for i in set1:
                        print(' ' + str(i), end='')
                    print('\n')
                elif cmd==16:
                    start = int(input("Enter the starting node of the edge : "))
                    end = int(input("Enter the ending node of the edge : "))
                    print("The cost is: "+ str(self._graph.get_cost(start, end)))
                elif cmd==17:
                    self._graph.critical_activities()
            except ValueError as ve:
                print(str(ve))







