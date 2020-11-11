#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# [x] first time 20-11-10: read other solutions and code by yourself
# [x] second time 20-11-10: select the best solution and use cpp to implement it
# [x] third time 20-11-10: after 24 hours
# [] forth time 20-11-10: after a week
# [] fifth time 20-11-10: before interview
# @lc code=start
class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                if not stack:
                    return False
                if char == ')' and stack[-1] =='(':
                    stack.pop()
                elif char == '}' and stack[-1] =='{':
                    stack.pop()
                elif char == ']' and stack[-1] =='[':
                    stack.pop()
                else:
                    return False
            else:
                pass
        if not stack:
            return True
        else:
            return False
# @lc code=end

sol = Solution()
print(sol.isValid("(])"))

