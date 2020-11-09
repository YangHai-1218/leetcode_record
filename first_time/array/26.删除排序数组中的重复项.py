#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# [x] first time 20-11-09: read other solutions and code by yourself
# [] second time 20-11-09: select the best solution and use cpp to implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# @lc code=start
# result: 
#   Your runtime beats 87.81 % of python3 submissions
#   Your memory usage beats 88.01 % of python3 submissions (14.3 MB)
# summary:
#   start_index is a pointer, 表示下一个不同元素存放的位置
#   当某一相同的元素遍历完之后，将该元素存放入start_index 表示的位置，且 start_index += 1
#   因此需要另外将列表最后的元素手动写入start_index指向的位置
# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
#         start_index = 0
#         for i, num in enumerate(nums):
#             num_ = nums[i-1] if i>0 else num
#             if num != num_:
#                 nums[start_index] = num_
#                 start_index += 1
        
#         nums[start_index] = num
#         return start_index + 1


# two pointer
# 相比于上面的版本更容易理解，
# 上面的版本利用的是当某一重复项遍历完时，相邻两元素不同
# 而该版本中，当开始遍历某一重复项时，会将该项复制到nums[j]，
# 因此只要nums[i]!=nums[j],此时表示该重复项遍历完
# 之后将下一个重复项复制到nums[j++]
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1
# @lc code=end
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))

