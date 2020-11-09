#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# [x] first time 20-11-09: read other solutions or code by yourself
# [x] second time 20-11-09: code by yourself or select the best solution and implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# @lc code=start

# Time Limit Exceeded
# class Solution:
#     def maxArea(self, height):
#         maxarea = 0
#         len_ = len(height)
#         for i in range(len_):
#             for j in range(i+1,len_):
#                 area = self.get_area(i,j,height)
#                 if area>maxarea:
#                     maxarea = area
#         return maxarea
#     def get_area(self,i,j,height):
#         min_height = min(height[i],height[j])
#         area = (j-i)*min_height
#         return area

class Solution:
    def maxArea(self, height):
        maxarea = 0
        len_ = len(height)
        i ,j = 0, len_-1
        while i<j:
            height_i, height_j = height[i], height[j]
            if height_i < height_j:
                minheight = height_i
                i += 1
            else:
                minheight = height_j
                j -= 1
            area = minheight * (j-i+1)
            maxarea = max(area,maxarea)

        return maxarea     

# @lc code=end

