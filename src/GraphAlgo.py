import json
import random

from src.GraphInterface import GraphInterface
from src.GrapthAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
'''Graph Algo class implements GraphAlgoInterface'''

class GraphAlgo(GraphAlgoInterface):

    '''Constructor'''
    def __init__(self, myGraph):
        myGraph = DiGraph()
        self.myGraph = myGraph
        '''New Graph'''

    def get_graph(self) -> GraphInterface:
        return self.myGraph

    '''Load'''
    def load_from_json(self, file_name: str) -> bool:
        try:
            '''Open file'''
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

    '''save'''
    def save_to_json(self, file_name: str) -> bool:
        pass

    '''Algorithms'''
