#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
from typing import List
# @lc code=start

# two-pointer
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        fast_pointer, slow_pointer = 1, 0
        max_len = 1
        while fast_pointer < len(nums):
            if nums[slow_pointer] < nums[fast_pointer]:
                cur_len = 1
                while fast_pointer < len(nums) and nums[slow_pointer] < nums[fast_pointer]:
                    fast_pointer += 1
                    slow_pointer += 1
                    cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                slow_pointer += 1
                fast_pointer += 1
        return max_len

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            if ans < dp[i]:
                ans = dp[i]
        return ans

# @lc code=end
Solution().findLengthOfLCIS([1,3,5,4,7])

