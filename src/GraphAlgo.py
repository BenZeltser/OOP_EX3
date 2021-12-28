import itertools
import json
import random
from typing import List
from sys import maxsize
from itertools import permutations

import length as length

from src.GraphInterface import GraphInterface
from src.GrapthAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.Heap import Heap, dijkstra

'''Graph Algo class implements GraphAlgoInterface'''

class GraphAlgo(GraphAlgoInterface):

    '''Constructor'''

    def __init__(self, myGraph):
        myGraph = DiGraph()
        self.myGraph = myGraph
        '''New Graph'''

    '''Get'''

    def get_graph(self) -> GraphInterface:
        return self.myGraph

    '''Load'''

    def load_from_json(self, file_name: str) -> bool:
        try:
            '''Open file as read'''
            with open(file_name, 'r') as f:
                load = json.load(f)
                '''Init graph instance'''
                myGraph: DiGraph = DiGraph()

                '''Iterate through nodes'''
                for i in load['Nodes']:
                    myGraph.add_node(i["id"])

                '''Iterate through edges'''
                for i in load['Edges']:
                    myGraph.add_edge(i["src"],i["dst"],i["weight"])

                '''Attribute the graph'''
                self.myGraph = myGraph

                f.close()
        except:
            raise NotImplementedError
        return True

    '''Save'''

    def save_to_json(self, file_name: str) -> bool:
        try:

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
                return True

        except:
            raise NotImplementedError


    '''Algorithms'''


    '''Shortest path - Implementation idea inspired by Wlliam Fiset '''

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        myGraph = self.myGraph
        return dijkstra(myGraph,id1,id2)

    '''TSP'''

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        myGraph = self.myGraph
        size = len(node_lst)
        vertex = []
        i=0
        while(i<size):
                vertex.append(i)
        min_path = maxsize
        next_permutation = permutations(vertex)
        for i in next_permutation:
            current_pathweight = 0
            k = size
            for j in i:
                current_pathweight += myGraph[k][j]
                k = j
            current_pathweight += myGraph[k][size]
            min_path = min(min_path, current_pathweight)
        return min_path

'''    def solve_tsp_dynamic(points):
        all_distances = [[length(x, y) for y in points] for x in points]
        A = {(frozenset([0, idx + 1]), idx + 1): (dist, [0, idx + 1]) for idx, dist in enumerate(all_distances[0][1:])}
        cnt = len(points)
        for m in range(2, cnt):
            B = {}
            for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
                for j in S - {0}:
                    B[(S, j)] = min([(A[(S - {j}, k)][0] + all_distances[k][j], A[(S - {j}, k)][1] + [j]) for k in S if
                                     k != 0 and k != j])
            A = B
        res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
        return res[1]'''


