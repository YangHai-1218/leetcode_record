#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start

# n^2 version
# class Solution:
#     def canJump(self, nums):
#         if len(nums) <= 1:
#             return True
#         num_back = [False for _ in nums]
#         for i,jump_time in enumerate(nums):
#             if jump_time == 0:
#                 if num_back[-1] == True:
#                     return True
#                 if num_back[i+1] == False:
#                     return False
#             num_back[i:i+jump_time+1] = [True for _ in range(jump_time+1)]
        
#         if num_back[-1] is True:
#             return True
#         else:
#             return False

# greedy version
class Solution:
    def canJump(self, nums):
        reachable = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= reachable:
                reachable = i
        return reachable == 0

# @lc code=end
sol = Solution()
print(sol.canJump([3,0,8,2,0,0,1]))

