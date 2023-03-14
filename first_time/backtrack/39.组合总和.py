#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.results = []
    def combinationSum(self, candidates, target):
        self.backtrack(candidates, target, 0, [])
        return self.results
    
    def backtrack(self, candidates, target, start_index, path):
        if sum(path) == target:
            self.results.append(path.copy())
            return 
        elif sum(path) > target:
            return
        
        for i in range(start_index, len(candidates)):
            path.append(candidates[i])
            self.backtrack(candidates, target, i, path)
            path.pop(-1)

            
            
# @lc code=end
candidates = [2,7,6,3,5,1]
target = 9
sol = Solution()
print(sol.combinationSum(candidates, target))
