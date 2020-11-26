#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
# Divide and conquer version
# class Solution:
    # def count(self, target, nums):
    #     result = 0
    #     for num in nums:
    #         if num == target:
    #             result += 1
    #     return result
    # def majorityElement(self, nums):
    #     if len(nums) == 1:
    #         return nums[0]
        
    #     len_next_nums = len(nums)//2
    #     left_mode = self.majorityElement(nums[0:len_next_nums])
    #     right_mode = self.majorityElement(nums[len_next_nums:])

    #     if left_mode ==  right_mode:
    #         return left_mode
    #     else:
    #         left_count = self.count(left_mode, nums)
    #         right_count = self.count(right_mode, nums)
    #         return left_mode if left_count>right_count else right_mode

# hash tabel version
class Solution:
    def majorityElement(self, nums):
        num_count = {'max':1,'max_num':nums[0]}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] +=1
            if num_count[num] > num_count['max']:
                num_count['max_num'] = num
                num_count['max'] = num_count[num]
        return num_count['max_num']
            
# @lc code=end
sol = Solution()
print(sol.majorityElement([6,6,6,7,7]))

