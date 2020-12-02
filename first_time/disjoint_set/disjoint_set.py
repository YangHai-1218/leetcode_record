
class DisjointSet:
    def __init__(self, n):
        self.p = [i for i in range(n)]
    
    def find(self, x):
        r = x
        while self.p[r] != r:
            r = self.p[r]
        # path compression
        i = x
        while i != r:
            j = self.p[i]
            self.p[i] = r
            i = j
        return r
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.p[rootx] = rooty
            
