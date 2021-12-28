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

