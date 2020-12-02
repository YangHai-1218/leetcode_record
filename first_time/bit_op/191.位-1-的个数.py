#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         result = 0
#         while n!=0 :
#             result += 1
#             n = n & (n-1)
#         return result


class Solution:
    def hammingWeight(self, n: int) -> int:
        n_ = bin(n)
        return n_.count('1')
       
# @lc code=end
