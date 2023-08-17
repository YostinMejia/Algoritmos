class WeightQuickUnion:

    def __init__(self, N:int) -> None:
        self.sz = []
        self.parent = []
        self.count = N

        for i in range(N):
            self.sz.append(1)
            self.parent.append(i)
        
    def root(self, i:int):
        
        while (i != self.parent[i]):
            i = self.parent[i]

        return i

    def union(self, p:int, q:int):

        rootP = self.root(p)
        rootQ = self.root(q)

        if (rootP == rootQ):return

        if (self.sz[rootP] < self.sz[rootQ]):
            self.parent[rootP] = rootQ
            self.sz[rootQ] += self.sz[rootP] 
        else:
            self.parent[rootQ] = rootP
            self.sz[rootP] += self.sz[rootQ] 
        
        self.count -=1
    
    def connected(self, p:int, q:int):
        return self.root(p) == self.root(q) 

            
