#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start

# [x] first time 20-12-06: read other solutions and code by yourself
# [x] second time 20-12-06: select the best solution and use cpp to implement it
# [] third time 20-12-06: after 24 hours
# [] forth time 20-12-06: after a week
# [] fifth time 20-12-06: before interview
class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        num_i = nums[0]-1
        self.res = 10**7
        for i, num in enumerate(nums):
            if num == num_i:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                if num + nums[left] + nums[right] > target:
                    self.update(nums, i, left, right, target)
                    num_right = nums[right]
                    right -= 1
                    while num_right == nums[right] and left < right:
                        right -= 1
                elif num + nums[left] + nums[right] < target:
                    self.update(nums, i, left, right, target)
                    num_left = nums[left]
                    left += 1
                    while num_left == nums[left] and  left < right:
                        left += 1
                else:
                    return target
        return self.res
    def update(self, nums, i, left, right, target):
        if abs(target - (nums[i] + nums[left] + nums[right])) < abs(target - self.res):
            self.res = (nums[i] + nums[left] + nums[right])
        

# @lc code=end
sol =  Solution()
print(sol.threeSumClosest( [-1,2,1,-4], 1))
