from DiGraph import DiGraph
from GraphAlgo import GraphAlgo



def check0():
    g = DiGraph()  # creates an empty directed graph
    g_algo = GraphAlgo(g)
    file = "data/A5.json"

    print("LOAD")
    g_algo.load_from_json(file)

    print("SAVE")
    g_algo.save_to_json(file + "_edited")

    print("CENTER")
    print(g_algo.centerPoint())

    print("TSP")
    print(g_algo.TSP([1, 2, 4]))

    print("PLOT")
    g_algo.plot_graph()

    print("SHORTEST")
    g_algo.shortest_path(0,1)


if __name__ == '__main__':
    check0()