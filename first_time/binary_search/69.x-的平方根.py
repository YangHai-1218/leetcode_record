#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x):
        left, right = 0, x 
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid 
        return right
        

# Newton version
# https://www.cnblogs.com/Allen-rg/p/13602550.html
# class Solution:
#     def mySqrt(self, x):
#         if x == 0:
#             return 0
#         x_new, x_old, C = 0, float(x), float(x)
#         while True:
#             x_new = (x_old + C/x_old) / 2
#             if abs(x_new - x_old) < 1e-6:
#                 break
#             x_old = x_new
#         return int(x_new)
        
# @lc code=end
# sol = Solution()
# print(sol.mySqrt(8))

# class Solution:

#     def Power(self, base, n):
#         if base==0:
#             return 0
#         if n==0:
#             return 1
#         left, right = 1, float('inf')
#         result = 1
#         while left <= right:
#             mid = ((left+ right)/2)
#             if mid**(1/n) == base:
#                 return mid
#             elif mid^(1/n) > left:
#                 result = mid
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return result

