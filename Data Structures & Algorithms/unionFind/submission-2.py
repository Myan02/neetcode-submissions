class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.num_components = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0 
        

    def find(self, x: int) -> int:
        p = self.parent[x]
        grand_p = self.parent[p]
        while p != grand_p:
            self.parent[p] = self.parent[grand_p]
            p = self.parent[p]
            grand_p = self.parent[p]
        return p


    def isSameComponent(self, x: int, y: int) -> bool:
        x_par = self.find(x)
        y_par = self.find(y)
        return x_par == y_par


    def union(self, x: int, y: int) -> bool:
        x_par, y_par = self.find(x), self.find(y)
        
        if x_par == y_par:
            return False

        if self.rank[x_par] > self.rank[y_par]:
            self.parent[y_par] = x_par
        elif self.rank[x_par] < self.rank[y_par]:
            self.parent[x_par] = y_par
        else:
            self.parent[y_par] = x_par
            self.rank[x_par] += 1
        self.num_components -= 1
        return True


    def getNumComponents(self) -> int:
        return self.num_components





