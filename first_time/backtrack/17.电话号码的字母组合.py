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
    
    def __init__(self) -> None:
        self.result = []
    def letterCombinations(self, digits) :
        if len(digits) == 0:
            return []
        self.backtrack([], digits, 0)
        return self.result

    def backtrack(self, path, digits, start_index):
        if len(path) == len(digits):
            self.result.append(''.join(path.copy()))
            return 
        
        chars = self.number_to_char_map[digits[start_index]]
        for c in chars:
            path.append(c)
            self.backtrack(path, digits, start_index+1)
            path.pop(-1)


# @lc code=end

sol = Solution()
print(sol.letterCombinations("999"))
