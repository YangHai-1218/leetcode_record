#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n):
        tar = n*n
        num = 1
        left, top, right, bottom = 0,0,n-1,n-1
        result = [[0]*n for _ in range(n)]
        while num <= tar:
            # from left to right
            i = left
            while i <= right and num <= tar:
                result[top][i] = num
                num += 1
                i += 1
            top += 1
            # from top to bottom
            i = top
            while i <= bottom and num <= tar:
                result[i][right] = num
                num += 1
                i += 1
            right -= 1
            # from right to left
            i = right
            while i >= left and num<= tar:
                result[bottom][i] = num
                num += 1
                i -= 1
            bottom -= 1
            # from bottom to top
            i = bottom
            while i >= top and num <= tar:
                result[i][left] = num
                num += 1
                i -= 1
            left += 1
        return result
# @lc code=end

sol = Solution()
print(sol.generateMatrix(3))

