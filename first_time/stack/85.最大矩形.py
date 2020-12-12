#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
# 84. 柱状图中最大的矩形
# https://leetcode-cn.com/problems/number-of-atoms/solution/python-dai-ma-qing-xi-by-hardcandy-b9qv/
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        maxarea = 0
        for j in range(rows):
            for i in range(cols):
                if matrix[j][i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            maxarea = max(maxarea, self.largestRectangleArea(heights))
               
        return maxarea

    def largestRectangleArea(self, heights):
        stack = [(-1,-1)]
        maxarea = 0
        for i, height in enumerate(heights):
            while height <= stack[-1][1]:
                _, height_ = stack.pop()
                area = height_ * (i - stack[-1][0] - 1)
                maxarea = max(area, maxarea)
            stack.append((i, height))

        stack.append((stack[-1][0]+1, -1))
        for idx,(_,height) in enumerate(stack):
            if height >=0 :
                area = height * (stack[-1][0] - stack[idx-1][0] -1)
                maxarea = max(area, maxarea)
        return maxarea
# @lc code=end

matrix = [["0","1"],["1","0"]]
sol = Solution()
print(sol.maximalRectangle(matrix))