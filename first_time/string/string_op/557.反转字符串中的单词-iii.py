#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_ = s.split()
        result = ''
        for i, word in enumerate(s_):
            word = ''.join(list(reversed(list(word))))
            if i == 0:
                result += word
            else:
                result += ' '+word
        return result
        
# @lc code=end

