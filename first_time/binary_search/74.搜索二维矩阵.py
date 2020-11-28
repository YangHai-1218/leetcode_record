#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        # first search along y axis, determine the possible row
        y_axis = [row[0] for row in matrix]
        left, right = 0, len(y_axis)-1
        while left <= right:
            mid = int((left+right)/2)
            if y_axis[mid] == target:
                return True
            elif y_axis[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # then search the target in searched possible row
        possible_row_index = right
        possible_row = matrix[possible_row_index]
        left, right = 0, len(possible_row)-1
        while left <= right:
            mid = int((left + right) / 2)
            if possible_row[mid] == target:
                return True
            elif possible_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# @lc code=end

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],50))