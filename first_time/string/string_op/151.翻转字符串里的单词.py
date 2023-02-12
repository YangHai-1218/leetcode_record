#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = self.removespace(s)
        s = s[::-1]
        start = 0
        for i in range(len(s)+1):
            if i == len(s) or s[i] == ' ':
                s[start:i] = s[start:i][::-1]
                start = i+1
        return ''.join(s)
        

    def removespace(self, s:str):
        s = list(s)
        fast_pointer, slow_pointer = 0, 0
        while fast_pointer < len(s):
            if s[fast_pointer] != ' ':
                if slow_pointer != 0:
                    s[slow_pointer] = ' '
                    slow_pointer += 1
                while fast_pointer < len(s) and s[fast_pointer] != ' ':
                    s[slow_pointer] = s[fast_pointer]
                    fast_pointer += 1
                    slow_pointer += 1
            fast_pointer += 1
        return s[:slow_pointer]

# @lc code=end
s ="  hello world"
sol  =Solution()
print(sol.reverseWords(s))