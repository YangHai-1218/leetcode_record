#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List
# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking([], n, k, 1)
        return self.result

    def backtracking(self, path:List, n:int, k:int, start_index:int):
        if len(path) == k:
            self.result.append(path.copy())
            return
        
        for i in range(start_index, n+1):
            path.append(i)
            self.backtracking(path, n, k, i+1)
            path.pop(-1)
# @lc code=end
print(Solution().combine(3, 3))

