#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s):
        map1 ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        len_s = len(s)
        map2 = {'IV':-2, 'IX':-2, 'XC':-20, 'XL':-20, 'CM':-200, 'CD':-200}
        for i,character in enumerate(s):
            num += map1[character]
            if i < len_s - 1:
                character_ = character+s[i+1]
                if character_ in map2:
                    num += map2[character_]
        return num
# @lc code=end

solution = Solution()
print(solution.romanToInt("MCMXCIV"))