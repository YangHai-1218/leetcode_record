#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates, target):

        self.res = []
        cur_state = []
        index = 0
        candidates = sorted(candidates)
        self._combinationSum(candidates, target, cur_state, index)
        return self.res
    def _combinationSum(self, candidates, target, cur_state, index):
        if target < candidates[0]:
            return 
        for index in range(index, len(candidates)):
            candidate = candidates[index]
            if candidate == target:
                cur_state.append(candidate)
                self.res.append(cur_state.copy())
                cur_state.pop()
                break
            else:
                cur_state.append(candidate)
                self._combinationSum(candidates, target-candidate, cur_state, index)
                cur_state.pop()
            
            
# @lc code=end
candidates = [2,7,6,3,5,1]
target = 9
sol = Solution()
print(sol.combinationSum(candidates, target))
