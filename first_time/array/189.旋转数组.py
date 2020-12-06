#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# [x] first time 20-11-09: read other solutions and code by yourself
# [] second time 20-11-09: select the best solution and use cpp to implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# @lc code=start
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k==0:
            return nums
        time = 0
        len_nums = len(nums)
        
        for start in range(len_nums):
            num_current = nums[start]
            index = (start+k)%len_nums


            while True:
                time += 1
                num_prev = nums[index]
                nums[index] = num_current
                if start==index:
                    break
                index = (index+k)%len(nums)
                num_current = num_prev
            if time==len_nums:
                break


# @lc code=end

sol = Solution()
print(sol.rotate([-1,-100,3,99],2))

