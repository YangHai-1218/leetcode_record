#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        if len(nums) <=2:
            return 1
        border_index = 0
        step = 0
        for i,jump_time in enumerate(nums):
            if i != border_index:
                continue
            step += 1
            border_index = i + jump_time
            if border_index >= len(nums) -1 :
                return step
            max_distance = nums[border_index] + border_index
            for j in range(i+1,i+jump_time+1):
                if nums[j] + j > max_distance:
                    max_distance = nums[j] + j
                    border_index = j
            if max_distance >= len(nums)-1:
                step += 1
                return step
        return step
# @lc code=end
sol = Solution()
print(sol.jump([3,2,1]))

