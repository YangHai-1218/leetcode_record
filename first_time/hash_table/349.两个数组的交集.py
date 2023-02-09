#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
from typing import List
# @lc code=start
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1) & set(nums2))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = [0 for _ in range(1000+1)]
        for n in nums1:
            record[n] = 1
        res = set()
        for n in nums2:
            if record[n] == 1:
                res.add(n)
        return list(res)
# @lc code=end

