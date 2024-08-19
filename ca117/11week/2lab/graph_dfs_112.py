#!/usr/bin/env python3

class Graph(object):
    
    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(V):
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v] = w
        self.adj[w] = v


class DFSPaths(object):
    
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * g.V
        self.parent = [-1] * g.V
        self.dfs(s)

    def dfs(self, v):
        queue = [v]
        self.visited[v] = True
        while queue:
            queue.pop(0)
        for w in self.g.adj[v]:
            if not self.visited[w]:
                queue.append(w)
                self.parent[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return []
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]

    def shortest(self, v):

