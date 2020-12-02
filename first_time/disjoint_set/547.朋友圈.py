#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
# 等同于岛屿数量问题

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

class Solution:
    def findCircleNum(self, M):
        n = len(M)
        self.disjointset = DisjointSet(n)
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.disjointset.union(i,j)
        return len(set([self.disjointset.find(i) for i in range(n)]))


# @lc code=end

