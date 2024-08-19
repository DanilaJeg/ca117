#!/usr/bin/env python3

import sys

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(V):
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFS(object):

    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * graph.V
        self.parent = [-1] * graph.V
        self.islandCount = self.Count()
    '''
    def hasPath(self, start, search):
        self.visited = [False] * self.graph.V
        self.dfs(start)
        return self.visited[search]

    def pathTo(self, search, start=0):
        self.visited = [False] * self.graph.V
        self.parent = [-1] * self.graph.V
        self.dfs(start)
        if not self.visited[search]:
            return []
        path = [search]
        while search != start:
            search = self.parent[search]
            path.append(search)
        return path[::-1]
    '''

    def dfs(self, node):
        self.visited[node] = True
        for neighbour in self.graph.adj[node]:
            if not self.visited[neighbour]:
                self.parent[neighbour] = node
                self.dfs(neighbour)
    
    def Count(self):
        count = 0
        for v in range(self.graph.V):
            if not self.visited[v]:
                self.dfs(v)
                count += 1 
        return count

V = int(sys.stdin.readline().strip())
g = Graph(V)
for line in sys.stdin:
    v, w = int(line.strip().split()[0]), int(line.strip().split()[1])
    g.addEdge(v, w)

dfs = DFS(g)
print(dfs.islandCount)

