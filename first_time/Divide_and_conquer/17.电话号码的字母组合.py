#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    number_to_char_map = {'2':['a','b','c'], 
                            '3':['d','e','f'],
                            '4':['g','h','i'],
                            '5':['j','k','l'],
                            '6':['m','n','o'],
                            '7':['p','q','r','s'],
                            '8':['t','u','v'],
                            '9':['w','x','y','z']}
    def letterCombinations(self, digits) :
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.number_to_char_map[digits[0]]
        
        current_digit = digits[-1]
        result = self.letterCombinations(digits[:-1])
        current_char = self.number_to_char_map[current_digit]
        result_ = result.copy()
        result = []
        for char in current_char:
            result += [l+char for l in result_]
        return result

# @lc code=end

sol = Solution()
print(sol.letterCombinations("999"))
