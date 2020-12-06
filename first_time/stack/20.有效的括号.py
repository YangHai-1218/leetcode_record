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
        temp = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in temp:
                stack.append(temp[char])
            else:
                if not stack:
                    return False
                if stack.pop(-1) != char:
                    return False
        if stack:
            return False
        else:
            return True


            
# @lc code=end

sol = Solution()
print(sol.isValid("(])"))

