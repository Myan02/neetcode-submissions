class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        p = self.par[x]
        if p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        union_tree = UnionFind(len(edges))  # build union tree

        # check each pair of vertices
        for edge in edges:
            v1, v2 = edge

            # if a cycle is found, return that edge
            if not union_tree.union(v1, v2):
                return edge










        