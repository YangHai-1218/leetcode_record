#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        reverse_x = int(str(x)[::-1])
        return reverse_x == x
# @lc code=end

solution = Solution()
print(solution.isPalindrome(121)) 