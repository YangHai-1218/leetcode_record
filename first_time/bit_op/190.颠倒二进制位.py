#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n):
        ans = 0
        for _ in range(32):
            ans = (ans << 1) + (n & 1)
            n = n >> 1
        return ans
        
# @lc code=end

