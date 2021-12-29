import json
import GraphInterface
import Edge
import Node


class DiGraph:

    def __init(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.mc = 0;

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edges.length()

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:

        tempEdgeDict = {}
        for x in self.edges:
            tempEdge = self.edges[x]
            startId = tempEdge.getSRC()
            endId = tempEdge.getDST()
            if endId == id1:
                tempNode = self.nodes[startId]
                tempEdgeDict[startId] = tempNode
        return tempEdgeDict

    def all_out_edges_of_node(self, id1: int) -> dict:
        tempEdgeDict = {}
        for x in self.edges:
            tempEdge = self.edges[x]
            startId = tempEdge.getSRC()
            endId = tempEdge.getDST()
            if startId == id1:
                tempNode = self.nodes[startId]
                tempEdgeDict[startId] = tempNode
        return tempEdgeDict

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.checkEdge(id1,id2) !=-1:
            return False
        edge = Edge(id1, id2, weight)
        self.edges.append(edge)
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id)== None:
            node = Node(node_id,pos)
            self.nodes[node_id]=node
            return True
        return False




    def remove_node(self, node_id: int) -> bool:
        if self.nodes.get(node_id)==None:
            return False
        self.nodes.pop(node_id)

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        location=self.checkEdge(node_id1, node_id2)
        if location==-1:
            return False
        self.edges.remove(location)
        return True

    """
    this function checks is an edge is already in the edge list and return True if it is 
    """
    def checkEdge(self, id1: int, id2: int) ->int:
        for x in self.edges:
            tempEdge= self.edges[x]
            startId=tempEdge.getSRC()
            endId=tempEdge.getDST()
            if id1==startId and endId==id2:
               return x
            return -1



