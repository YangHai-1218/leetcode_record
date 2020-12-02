#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
# 二进制形式有且仅有一个1
class Solution:
    def isPowerOfTwo(self, n):
        if n== 0:
            return False
        n = n &(n-1)
        return True if n==0 else False
# @lc code=end

sol = Solution()
print(sol.isPowerOfTwo(6))