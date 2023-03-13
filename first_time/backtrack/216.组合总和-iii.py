#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
from typing import List
# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack([], n, k, 1)
        return self.result

    def backtrack(self, path:List, n:int, k:int, start_index:int):
        if len(path) == k:
            if sum(path) == n:
                self.result.append(path.copy())
            return 

        if sum(path) > n:
            return
        
        for i in range(start_index, 9+1):
            path.append(i)
            self.backtrack(path, n, k, i+1)
            path.pop(-1)
        


# @lc code=end

print(Solution().combinationSum3(9, 45))