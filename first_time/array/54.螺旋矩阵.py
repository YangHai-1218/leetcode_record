#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        left, top, right, bottom = 0, 0, len(matrix[0])-1, len(matrix)-1
        result = []
        while True:
            # from left to right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            # from top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            # from right to left 
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
        
            # from bottom to top
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right:
                break
            
        return result
# @lc code=end

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
sol = Solution()
print(sol.spiralOrder(matrix))