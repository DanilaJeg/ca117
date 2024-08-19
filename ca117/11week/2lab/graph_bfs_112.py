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


class BFSPaths(object):

   def __init__(self, g, s):
      self.g = g
      self.s = s
      self.marked = [False] * g.V
      self.parent = [-1] * g.V
      self.bfs(s)

   def bfs(self, s):
      queue = [s]
      self.marked[s] = True

      while queue:
         v = queue.pop(0)
         for w in self.g.adj[v]:
            if not self.marked[w]:
               queue.append(w)
               self.parent[w] = v
               self.marked[w] = True

   # Return True if there is a path from s to v
   def hasPathTo(self, v):
      return self.marked[v]

   # Return path from s to v (or [] should one not exist)
   def pathTo(self, v):
      if not self.hasPathTo(v):
         return []
      path = [v]
      while v != self.s:
         v = self.parent[v]
         path.append(v)
      return path[::-1]
