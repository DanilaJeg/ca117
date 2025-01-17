#!/usr/bin/env python3

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(V):
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max(len(self.adj[v]) for v in self.adj)

    def avgDegree(self):
        return sum(len(self.adj[v]) for v in self.adj) / self.V


