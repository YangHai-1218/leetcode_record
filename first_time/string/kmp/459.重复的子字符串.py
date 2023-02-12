#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_s =  s+s
        return (new_s[1:-1]).find(s) != -1
# @lc code=end
Solution().repeatedSubstringPattern('bb')

