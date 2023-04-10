#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        pass

        def _dfs(index, current_number):
            current_index_number = current_number[index]
            for number in range(current_index_number+1, 11):
                current_number[index] = number
                if ''.join(list(map(str, current_number))) in de

            



# @lc code=end

