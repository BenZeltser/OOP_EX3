import src

import sys

import heapq as heapQueue

from src.DiGraph import DiGraph
from src.Node import Node

'''Idea inspired by the way of DR. William Fiset - GitHub & Youtube'''
def Dijkstra(myGraph: DiGraph, src: int, dest: int) -> (float, list):
    maxVal = sys.maxsize #Max_value
    distance_list = {Node: maxVal for Node in myGraph.get_all_v()}

    distance_list[src] = 0
    prev_nodes = {src: maxVal}
    NodeQueued = []
    heapQueue.heappush(NodeQueued, (0, src))

    while NodeQueued:
        curr_node = heapQueue.heappop(NodeQueued)[1]

        if distance_list[curr_node] == maxVal:break
        edges = myGraph.all_out_edges_of_node(curr_node)
        #Approximated Nodes thy neighbor
        for i in edges.keys():
            new_path = distance_list[curr_node] + edges.get(i).key
            if new_path < distance_list[i]:

                distance_list[i] = new_path
                prev_nodes[i] = curr_node
                heapQueue.heappush(NodeQueued, (distance_list[i], i))
            if curr_node == dest:
                break

    if distance_list[dest] == maxVal:
        return float('inf'), []
    backTrack = []
    curr_node = dest

    while curr_node != src:
        backTrack.insert(0, curr_node)
        curr_node = prev_nodes[curr_node]

        #Check the backtrack trace
    if backTrack:
        backTrack.insert(0, curr_node)
    return (distance_list[dest] / 1.0,backTrack)
