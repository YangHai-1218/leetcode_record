#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
# 思路
# 遇到左括号，数字，char就push入栈
# 遇到右括号，开始出栈，直到遇到左括号，注意这里pop出来的都是char，将pop出来的char组成string
#   之后将左括号也pop
#   之后我们要计算这个string需要重复多少次
#   将所有的数字pop出来，计算出需要重复的次数
#   将string重复后，再入栈
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                
                chars = []
                while stack[-1] != '[':
                    chars.append(stack.pop())
                stack.pop()
                chars = list(reversed(chars))

                nums,  pow10= 0, 0
                while stack and stack[-1].isdigit():
                    nums += int(stack.pop()) * 10 ** pow10
                    pow10 += 1

                stack.append("".join(chars)*int(nums))
            else:
                stack.append(char)
        return "".join(stack)
# @lc code=end

sol = Solution()
print(sol.decodeString("2[abc]3[cd]ef"))