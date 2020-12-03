#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = lambda x:x == x[::-1]
        strpart = lambda s,x: s[:x]+s[x+1:]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strpart(s,left)) or isPalindrome(strpart(s,right))
            left += 1
            right -= 1
        return True
# @lc code=end

