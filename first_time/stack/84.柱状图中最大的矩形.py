#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# [x] first time 20-11-10: read other solutions and code by yourself
# [] second time 20-11-10: select the best solution and use cpp to implement it
# [] third time 20-11-10: after 24 hours
# [] forth time 20-11-10: after a week
# [] fifth time 20-11-10: before interview
# @lc code=start

# violent solution I 
# class Solution:
#     def largestRectangleArea(self, heights):
#         if not heights:
#             return 0
#         if len(heights) == 1:
#             return heights[0]
#         maxarea = 0
#         n = len(heights)
#         for i in range(n):
#             for j in range(n-1,i-1,-1):
#                 minheight = self.get_min_height(heights,i,j)
#                 area = minheight * (j-i+1)
#                 maxarea = max(area,maxarea)
#         return maxarea

#     def get_min_height(self,heights,i,j):
#         minheight = heights[i]
#         for height in heights[i:j+1]:
#             minheight = min(height, minheight)
#         return minheight

# violent solution I 
# class Solution:
#     def largestRectangleArea(self, heights):
#         if not heights:
#             return 0
#         if len(heights) == 1:
#             return heights[0]
#         maxarea = 0
#         n = len(heights)
#         heights.append(0)
#         heights.insert(0,0)
#         for i in range(1,n+1):
#             minheight = heights[i]
#             right_bound, left_bound = i,i
#             for j in range(i+1,n+2):
#                 if heights[j] < minheight:
#                     right_bound = j
#                     break
#             for j in range(i-1,-1,-1):
#                 if heights[j] < minheight:
#                     left_bound = j
#                     break
#             area = minheight * (right_bound - left_bound - 1)
#             maxarea = max(area, maxarea)
#         return maxarea

# stack version
class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        
        stack = [(-1,-1)]
        maxarea = 0
        for i,height in enumerate(heights):
            while height <= stack[-1][1]:
                _, height_ = stack.pop()
                area = height_ * (i - stack[-1][0] - 1)
                maxarea = max(area, maxarea)

            stack.append((i,height))
        
        stack.append((stack[-1][0]+1,-1))
        for i,(_,height) in enumerate(stack):
            if height >= 0:
                area = (stack[-1][0] - stack[i-1][0] - 1)*height
                maxarea = max(area,maxarea)
        return maxarea

# stack version II

# @lc code=end


sol = Solution()
print(sol.largestRectangleArea([2,3]))
