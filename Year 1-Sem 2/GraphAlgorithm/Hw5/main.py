from itertools import chain


from Repo import Repo
from UI import UI




input_file = input("Enter the name of the input file: ")
graph = Repo(input_file)
ui = UI(graph)
ui.start_me()

save_after_modif = input("Save the modified graph in a new file: ")
vertices = graph.parse_graph()

with open(save_after_modif, 'wt') as f: # write text
    f.write(str(graph.nr_of_vertices()) + " " + str(graph.nr_edges()) + "\n")
    list_vertices = list(chain.from_iterable(graph._graph.edges))
    i = 0
    for x in range(graph.nr_edges()):
        start = list_vertices[i]
        end = list_vertices[i + 1]
        i = i + 2
        f.write(str(start) + " " + str(end) + "\n")

    for x in graph._graph.vertices.keys():
        if x not in list_vertices:
            f.write(str(x) + " ")

f.close()

