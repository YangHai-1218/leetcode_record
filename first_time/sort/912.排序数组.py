#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    

    def quickSort(self, nums, begin, end):
        if begin >= end:
            return nums
        pivot = self.partition(nums, begin, end)
        self.quickSort(nums, pivot+1, end)
        self.quickSort(nums, begin, pivot-1)
    
    def partition(self, nums, begin, end):
        pivot, pointer = end, begin
        for i in range(begin, end):
            if nums[i] < nums[pivot]:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        nums[pivot], nums[pointer] = nums[pointer], nums[pivot]
        return pointer
        
# @lc code=end


if __name__ == '__main__':
    array = [-1,2,-8,-10]
    solution = Solution()
    ans = solution.sortArray(array)
    print(ans)