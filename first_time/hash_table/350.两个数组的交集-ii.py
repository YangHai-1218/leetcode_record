#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record_nums1 = defaultdict(int)
        for n in nums1:
            record_nums1[n] += 1
        res = []
        for n in nums2:
            if n in record_nums1 and record_nums1[n] > 0:
                res.append(n)
                record_nums1[n] -= 1
        return res


# @lc code=end

