#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start

# corner case !!!!!
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s = list(s.strip())
        if len(s) == 0:
            return 0

        
        if s[0] == '-':
            sign = -1
            del s[0]
        elif s[0] == '+':
            sign = 1
            del s[0]
        elif  s[0].isdigit():
            sign = 1
        else:
            return 0

        ret, i = 0, 0
        while i< len(s) and s[i].isdigit():
            ret = ret*10 +int(s[i])
            i += 1
        return max(-2**31, min(sign*ret, 2**31-1))

            

# @lc code=end

s =  " "
sol = Solution()
print(sol.myAtoi(s))