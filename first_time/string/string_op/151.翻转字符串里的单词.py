#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_ = s.split()
        s_ = list(reversed(s_))
        len_s = len(s_)
        result = ''.join([word+' ' if i!=len_s-1 else word for i,word in enumerate(s_)])
        return result

# @lc code=end
s = "  Bob    Loves  Alice   "
sol  =Solution()
print(sol.reverseWords(s))