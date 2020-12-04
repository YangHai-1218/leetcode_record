#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
# 暴力求解
# 嵌套循环，找到所有的子串，判断子串是否是回文串
# 暴力求解优化
# 枚举回文字串的中心，向外扩张（回文子串一定是对称的

# version I

class Solution:
    def longestPalindrome(self, s: str) -> str:
# @lc code=end

