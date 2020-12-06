#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        n, m = len(matrix[0]), len(matrix)
        left, top, right, bottom = 0, 0, n-1, m-1
        num = 1
        tar = m * n
        result = []
        while num <= tar:
            # from left to right
            i = left
            while i <= right and num <= tar: 
                result.append(matrix[top][i])
                num += 1
                i += 1
            top += 1
            
            # from top to bottom
            i = top
            while i <= bottom and num <= tar:
                result.append(matrix[i][right])
                num += 1
                i += 1
            right -= 1

            # from right to left
            i = right
            while i >= left and num <= tar:
                result.append(matrix[bottom][i])
                num += 1
                i -= 1
            bottom -= 1
            
            # from bottom to top
            i = bottom
            while i>= top and num <= tar:
                result.append(matrix[i][left])
                num += 1
                i -= 1
            left += 1
        return result
# @lc code=end

matrix = [
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8],
 [ 9, 10,11, 12]
]
sol = Solution()
print(sol.spiralOrder(matrix))