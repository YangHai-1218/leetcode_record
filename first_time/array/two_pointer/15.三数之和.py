#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# [x] first time 20-11-09: code by yourself and read other solutions
# [] second time 20-11-09: select the best solution and implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# tag: array two-pointers
# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # 如果第一个数大于0，由于后面的数大于第一个数，和不可能为0
                break
            if i > 0 and nums[i] == nums[i-1]:
                # 重复的数略过
                continue
            # 双指针寻找sum(nums[left] + nums[right]) = -nums[i]
            left, right = i+1, len(nums) - 1
            while left < right:
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < len(nums)-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left, right = left+1, right-1
        return res





# @lc code=end


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
