from Graph import generate_a_random_graph
from Repo import Repo
from UI import UI


done=False
while not done:
    cmd =int(input("How do you want to read the graph? 1.from file  2.from console\n "))
    if cmd == 1:
        input_file = input("Enter the name of the input file: ")
        graph = Repo(input_file)
        done=True
    elif cmd==2:
        nr_vertices = int(input("Enter the nr of vertices>>>"))
        nr_edges = int(input("Enter the nr of edges>>>"))
        graph = generate_a_random_graph(nr_vertices, nr_edges)
        done=True
    else:
        print("Bad command")


ui = UI(graph)
ui.start_me()

save_after_modif = input("Save the modified graph in a new file: ")
vertices = graph.parse_graph()

with open(save_after_modif, "w+") as f:
    f.write(str(graph.nr_of_vertices()) + ' ' + str(graph.nr_of_edges()) + "\n")
    for i in vertices:
        for j in graph.parse_out(i):
            cost = graph.get_cost(i, j)
            f.write(str(i) + ' ' + str(j) + ' ' + str(cost) + "\n")
        if (graph.get_in_out_degree(i)==(0,0)):
            f.write(str(i) +"\n")

f.close()
