import time

import array
import errno
import itertools
import json
import random
from typing import List
from sys import maxsize
from itertools import permutations

from matplotlib import pyplot as plt

from src import FloydWarshallAlgo
import DiGraph
start = time.time()

from src.GraphInterface import GraphInterface
from src.GrapthAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.Heap import Heap, dijkstra

'''Graph Algo class implements GraphAlgoInterface'''

class GraphAlgo(GraphAlgoInterface):
    start = time.time()
    '''Constructor'''

    def __init__(self, myGraph: DiGraph = DiGraph()):
        '''New Graph'''
        self.myGraph = myGraph
        print(start-time.time())



    '''Get'''

    def get_graph(self) -> GraphInterface:
        start = time.time()
        return self.myGraph
        print(get)
        print(start - time.time())

    '''Load'''

    def load_from_json(self, file_name: str) -> bool:
        try:
            start = time.time()
            '''Open file as read'''
            with open(file_name, 'r') as f:
                load = json.load(f)
                '''Init graph instance'''
                myGraph: DiGraph = DiGraph()

                '''Iterate through nodes'''
                for i in load['Nodes']:
                    if "pos" not in i:
                        myGraph.add_node(i["id"])

                '''Iterate through edges'''
                for i in load['Edges']:
                    myGraph.add_edge(i["src"],i["dst"],i["weight"])

                '''Attribute the graph'''
                self.myGraph = myGraph

                f.close()
        except:
            return errno
        print("load")
        print(start - time.time())
        return True

    '''Save'''

    def save_to_json(self, file_name: str) -> bool:

        try:
            start = time.time()
            '''Create Dict parameters (dynamic ds)'''
            jdict = {'Edges': [], 'Nodes': []}

            '''Open (create) Json file as write'''
            with open(file_name, 'w') as f:

                '''Iterate in a nested loop. \n
                   Append edges.'''

                for i in self.get_graph().get_all_v().keys():
                    for j,k in self.get_graph().all_in_edges_of_node(i).items():
                        jdict['Edges'].append(
                            {'src': i, 'dst': j, 'w': k})


                '''append nodes'''

                for i in self.get_graph().get_all_v().values():
                    jdict['Nodes'].append(
                        {'id':i.key}
                    )

                '''Apply the data to the file'''
                size = len(jdict)
                out = json.dumps(jdict, allow_nan=True, indent=size)
                f.write(out)

                '''-> Condit'''
                print("save:")
                print(start - time.time())
                return True

        except:
            return errno


    '''******Algorithms******'''


    '''Shortest path - Implementation idea inspired by Wlliam Fiset '''

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        start = time.time()
        myGraph = self.myGraph
        if (dijkstra(myGraph,id1,id2)) is None:
            return [float('inf'),float('inf')]
        else:
            return dijkstra(myGraph,id1,id2)

    '''TSP'''

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        start = time.time()
        myGraph = self.myGraph
        size = len(node_lst)
        vertex = []
        i=0
        while(i<size):
                vertex.append(i)
                i = i + 1
        min_path = maxsize
        next_permutation = permutations(vertex)

        for i in next_permutation:
            current_pathweight = 0
            k = size
            for j in i:
                if (myGraph.get_all_v().get(j) is None):
                    current_pathweight = current_pathweight+0
                else:
                    current_pathweight += myGraph.get_all_v().get(j).key
                k = j
            if (myGraph.get_all_v().get(k) is None):
                current_pathweight = current_pathweight+0
            else:
                current_pathweight += myGraph.get_all_v().get(k).key
            min_path = min(min_path, current_pathweight)
        print("Shortest Path")
        print(start - time.time())
        return min_path

    '''Center'''

    def centerPoint(self) -> (int, float):
        start = time.time()
        '''Here we will use the Floyd-Warshall algorithm
            and we will return the minimum element'''
        nodeKeys = []
        edgeKeys = []
        n = self.myGraph.get_all_v().__sizeof__()
        e = self.myGraph.get_edges().__sizeof__()
        for i in range(0,n):
            nodeKeys.append(self.myGraph.get_all_v().get(i))
        for edge in self.myGraph.get_edges():
            edgeKeys.append(edge.src)
        ans = FloydWarshallAlgo.floyd_warshall(len(nodeKeys),len(edgeKeys))

        print("Center")
        print(start - time.time())
        return ans

    '''Plot Graph'''
    def plot_graph(self) -> None:
        X = []
        Y = []
        all_nodes = self.myGraph.get_all_v()
        for x in range(len(self.myGraph.get_all_v())):
            node = all_nodes[x]
            X.append(node.getX())
            Y.append(node.getY())
        plt.plot(X, Y)
        plt.plot(X, Y, 'ro')
        plt.show()






