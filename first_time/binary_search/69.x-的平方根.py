#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
# class Solution:
#     def mySqrt(self, x):
#         if x == 0:
#             return 0
#         left, right = 1, x
#         result = -1
#         while left <= right:
#             mid = int(left + (right - left) / 2)
#             if mid**2 == x:
#                 return mid
#             elif mid ** 2 >x:
#                 right = mid - 1
#             else:
#                 result = mid
#                 left = mid + 1
#         return result

# Newton version
class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        x_new, x_old, C = 0, float(x), float(x)
        while True:
            x_new = (x_old + C/x_old) / 2
            if abs(x_new - x_old) < 1e-6:
                break
            x_old = x_new
        return int(x_new)
        
# @lc code=end
sol = Solution()
print(sol.mySqrt(8))

