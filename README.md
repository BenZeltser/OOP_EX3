# OOP_EX3

![Types-of-Methods-in-Python](https://user-images.githubusercontent.com/92685838/147823356-0ce68f52-09fe-4d93-8217-ffa7c6132fbc.jpg)


## Introduction 📥
![הורדה](https://user-images.githubusercontent.com/92685838/147823836-9c5ecfc2-d70d-4321-a537-0e162ac23a9e.png)



#### This project is the 4th of a 5 series projects within OOP course in Ariel University, class of 2021-2022.  
#### on this Project we implement Graphs, Graph Algorithms and Graph plots using Python3. 

#### as mentioned, on this project we will write a Python program that will focus on Graph theory
#### by implementing the ideas the principles that we learn in the Object oriented programming course.
#### The program will present a Directed weighted graph using a Json file that speficies it's nodes and edges and it's  Geographical coordinates.



### For further Information regarding the program features see the page's [Wiki](https://github.com/BenZeltser/OOP_EX3/wiki)


## Program Structure 🏗️

the program is completely Python based. the different classes and Interfaces and how they interact with each other is well obliged to have an amended explanation using a [UML Diagram](https://he.wikipedia.org/wiki/Unified_Modeling_Language)

## Algorithms 🌀

#### Dijkstra's algorithm - 
Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in the given graph.
Dijkstra’s algorithm is very similar to Prim’s algorithm for minimum spanning tree. Like Prim’s MST, we generate a SPT (shortest path tree) with a given source as a root. We maintain two sets, one set contains vertices included in the shortest-path tree, other set includes vertices not yet included in the shortest-path tree. At every step of the algorithm, we find a vertex that is in the other set (set of not yet included) and has a minimum distance from the source.
Below are the detailed steps used in Dijkstra’s algorithm to find the shortest path from a single source vertex to all other vertices in the given graph. 

#### Traveling Salesman Problem (TSP) - 

Given a set of cities and distances between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point. 
Note the difference between Hamiltonian Cycle and TSP. The Hamiltonian cycle problem is to find if there exists a tour that visits every city exactly once. Here we know that Hamiltonian Tour exists (because the graph is complete) and in fact, many such tours exist, the problem is to find a minimum weight Hamiltonian Cycle. 
For example, consider the graph shown in the figure on the right side. A TSP tour in the graph is 1-2-4-3-1. The cost of the tour is 10+25+30+15 which is 80.
The problem is a famous NP-hard problem. There is no polynomial-time known solution for this problem. 


#### Graph center - 

The center (or Jordan center) of a graph is the set of all vertices of minimum eccentricity, that is, the set of all vertices u where the greatest distance d(u,v) to other vertices v is minimal. Equivalently, it is the set of vertices with eccentricity equal to the graph's radius. Thus vertices in the center (central points) minimize the maximal distance from other points in the graph.
