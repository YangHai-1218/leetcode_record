#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
# result: 
#   Your runtime beats 87.81 % of python3 submissions
#   Your memory usage beats 88.01 % of python3 submissions (14.3 MB)
# summary:
#   start_index is a pointer, 表示下一个不同元素存放的位置
#   当某一相同的元素遍历完之后，将该元素存放入start_index 表示的位置，且 start_index += 1
#   因此需要另外将列表最后的元素手动写入start_index指向的位置
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        start_index = 0
        for i, num in enumerate(nums):
            num_ = nums[i-1] if i>0 else num
            if num != num_:
                nums[start_index] = num_
                start_index += 1
        
        nums[start_index] = num
        return start_index + 1
# @lc code=end
solution = Solution()
nums = [0,0,1,3,4,5,6,6,7,7]
solution.removeDuplicates(nums)

