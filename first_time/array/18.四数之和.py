#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# [x] first time 20-12-06: read other solutions and code by yourself
# [x] second time 20-12-06: select the best solution and use cpp to implement it
# [] third time 20-12-06: after 24 hours
# [] forth time 20-12-06: after a week
# [] fifth time 20-12-06: before interview
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        res = []
        num_i = nums[0]-1
        for i in range(len(nums)-1):
            if nums[i] == num_i:
                continue
            num_i = nums[i]
            num_j = nums[i+1] - 1
            for j in range(i+1, len(nums)):
                if nums[j] == num_j:
                    continue
                num_j = nums[j]
                left, right = j+1, len(nums)-1
                while left < right:
                    four_sum = num_i + num_j + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        num_left, num_right = nums[left], nums[right]
                        left, right = left+1, right +1
                        while nums[left] == num_left and left < right:
                            left += 1
                        while nums[right] == num_right and left < right:
                            right -= 1
                    elif four_sum < target:
                        num_left = nums[left]
                        left += 1
                        while nums[left] == num_left and left < right:
                            left += 1
                    elif four_sum > target:
                        num_right = nums[right]
                        right -= 1
                        while nums[right] == num_right and left < right:
                            right -= 1
        return res
# @lc code=end

