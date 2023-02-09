#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        record_nums1_nums2 = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                record_nums1_nums2[n1+n2] += 1
            
        for n3 in nums3:
            for n4 in nums4:
                if 0-n3-n4 in record_nums1_nums2:
                    ans += record_nums1_nums2[0-n3-n4]
        return ans

# @lc code=end

