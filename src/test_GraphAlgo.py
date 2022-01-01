from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.Node import Node


class Test(TestCase):

    def test_graph_algo(self):

        x = Node(0,None)
        y = Node(None,0)

        a = Node(0, 2)
        a = Node(0, 3)
        a = Node(0, 4)
        a = Node(0, 5)
        a = Node(0, 6)
        a = Node(0, 7)
        a = Node(0, 8)
        a = Node(0, 9)
        a = Node(0, 10)
        a = Node(1, 1)
        a = Node(12, 1)
        a = Node(13, 1)
        a = Node(14, 1)
        a = Node(15, 1)
        a = Node(16, 1)
        a = Node(1234, 1)
        a = Node(1232, 1)
        a = Node(12323, 1)
        myGraph = DiGraph()
        myGraphAlgo = GraphAlgo(myGraph)
        myGraphAlgo.get_graph()
        graph = myGraphAlgo.get_graph()
        self.assertEqual(myGraph,graph)
        myGraphAlgo.get_graph().add_node(15,1)
        myGraphAlgo.get_graph().add_edge(1,2,3.0)

    def testDijkestra(self):
        x = Node(0, None)
        y = Node(1, None)
        z = Node(2, None)
        w = Node(3, None)
        k = Node(4, None)
        graph = DiGraph()
        algo = GraphAlgo(graph)
        algo.get_graph().add_node(x.key, x.key)
        algo.get_graph().add_node(y.key, y.key)
        algo.get_graph().add_node(z.key, z.key)
        algo.get_graph().add_node(w.key, w.key)
        algo.get_graph().add_node(k.key, k.key)
        algo.get_graph().add_node(x.key, x.key)
        algo.get_graph().add_edge(1, 1, 5.0)
        algo.get_graph().add_edge(2, 2, 6.0)
        algo.get_graph().add_edge(3, 3, 8.0)
        algo.get_graph().add_edge(4, 4, 9.0)
        algo.get_graph().add_edge(5, 5, 11.0)
        algo.get_graph().add_edge(6, 6, 12.0)
        algo.get_graph().add_edge(0, 7, 13.0)
        algo.get_graph().add_edge(0, 8, 17.0)
        algo.get_graph().add_edge(0, 9, 18.0)
        algo.get_graph().add_edge(0, 10, 19.0)
        algo.get_graph().add_edge(0, 11, 20.0)
        algo.get_graph().add_edge(0, 12, 22.0)
        algo.get_graph().add_edge(0, 13, 25.0)

    def testPlotGraph(self):
        A0= "data/A0.json"
        A1 = "data/A1.json"
        A2 = "data/A2.json"
        A3 = "data/A3.json"
        A4 = "data/A4.json"
        A5 = "data/A5.json"
        A6 = "data/A6.json"

        graph = DiGraph()
        algo = GraphAlgo(graph)

        algo.plot_graph()
        algo.load_from_json(A0)

        algo.plot_graph()
        algo.load_from_json(A1)

        algo.plot_graph()
        algo.load_from_json(A2)

        algo.plot_graph()
        algo.load_from_json(A3)

        algo.plot_graph()
        algo.load_from_json(A4)

        algo.plot_graph()
        algo.load_from_json(A5)

        algo.plot_graph()
        algo.load_from_json(A6)

        algo.plot_graph()

