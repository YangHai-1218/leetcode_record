#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left_index, right_index = 0, 0
        types = defaultdict(int)
        result = 0
        while right_index < len(fruits):
            types[fruits[right_index]] += 1
            while len(types) > 2:
                types[fruits[left_index]] -= 1
                if types[fruits[left_index]] == 0:
                    types.pop(fruits[left_index])
                left_index += 1
            sub_len = right_index - left_index + 1
            result = sub_len if sub_len > result else result
            right_index += 1
        return result if result != 0 else len(fruits)    
# @lc code=end
print(Solution().totalFruit([1,2,3,2,2]))

