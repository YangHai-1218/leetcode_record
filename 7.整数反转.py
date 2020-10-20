#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
# stupid version
# class Solution:
#     def reverse(self, x):
#         reverse_num = 0
#         start = False
#         start_index = 0
#         negative = False
#         if x < 0:
#             negative = True
#             x = abs(x)
        
#         for i in range(30,-1,-1):
#             num = x // (10**i)
#             if num >= 1 and start == False:
#                 start = True
#             if start == True:
#                 reverse_num += num * 10**start_index
#                 start_index += 1
#                 x -= num * 10**i
#         if negative:
#             reverse_num = 0 - reverse_num
#         if reverse_num >= 2**31 or reverse_num < - 2**31:
#             return 0
#         return reverse_num

# smart version (invole str list convert)
# class Solution:
#     def reverse(self, x):
#         s = 1 if x>0 else -1
#         reverse_x = int(str(abs(x))[::-1])
        
#         return reverse_x * s * (reverse_x < 2**31)

# smart version II (pop)
class Solution:
    def reverse(self, x):
        s = 1 if x > 0 else -1
        x = abs(x)
        r = 0
        while x:
            r = x % 10 + r * 10
            x = x // 10
        return r * s * (r < 2 **31)
# @lc code=end

solution = Solution()
print(solution.reverse(1534236469))
