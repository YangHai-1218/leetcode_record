#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target):
        self.res = []
        cur_state = []
        index = -1
        candidates = sorted(candidates)
        self._combinationSum2(candidates, target, index, cur_state)
        return self.res
    def _combinationSum2(self, candidates, target, index, cur_state):
        if target < candidates[0]:
            return
        if index + 1 > len(candidates)-1:
            return
        
        candidate_i = candidates[index+1] - 1
        for i in range(index+1, len(candidates)):
            candidate = candidates[i]
            # 去重
            if candidate == candidate_i:
                continue
            if candidate == target:
                cur_state.append(candidate)
                self.res.append(cur_state.copy())
                cur_state.pop()
                break
            elif candidate > target:
                break
            else:
                cur_state.append(candidates[i])
                self._combinationSum2(candidates, target-candidate, i, cur_state)
                cur_state.pop()
            candidate_i = candidates[i]


# @lc code=end

candidates = [1]
sol = Solution()
print(sol.combinationSum2(candidates, 2))