from math import inf
from itertools import product
from random import random

def floyd_warshall(n, edge):

    u=v=w=k=i=j=0
    rn = range(n)
    dist = [[inf] * n for i in rn]
    nxt = [[0] * n for i in rn]
    breed = random()*100
    bread = (int)(breed)
    for i in rn:
        dist[i][i] = 0
    # for u, v, w in range(0,50):
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1
    # for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]

    ans = dist[i][j]
    return sum_ik_kj