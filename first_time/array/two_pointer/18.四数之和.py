#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, len(nums)-1
                while left < right:
                    if left > j+1 and nums[left] == nums[left-1]:
                        left += 1
                        continue
                    if right < len(nums) - 1 and nums[right] == nums[right+1]:
                        right -= 1
                        continue
                    
                    if nums[left] + nums[right] + nums[i] + nums[j] > target:
                        right -= 1
                    elif nums[left] + nums[right] + nums[i] + nums[j] < target:
                        left += 1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left, right = left+1, right-1
        return res
                
# @lc code=end

