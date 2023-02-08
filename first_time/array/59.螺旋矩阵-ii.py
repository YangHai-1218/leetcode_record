#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n):
        num = 1
        result = [[0]*n for _ in range(n)]
        loop = n // 2
        startx, starty = 0, 0 
        for offset in range(1, loop+1):
            for i in range(startx, n-offset):
                result[starty][i] = num
                num += 1
            for i in range(starty, n-offset):
                result[i][n-offset] = num
                num += 1
            for i in range(n-offset, startx, -1):
                result[n-offset][i] = num
                num += 1
            for i in range(n-offset, starty, -1):
                result[i][startx] = num
                num += 1
            startx += 1
            starty += 1
        if n % 2 != 0:
            result[n//2][n//2] = n**2
        return result
# @lc code=end

sol = Solution()
print(sol.generateMatrix(2))

