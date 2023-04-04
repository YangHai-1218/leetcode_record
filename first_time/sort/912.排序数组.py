#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums):
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j - 1)
            quick(j + 1, right)
            return nums

        return quick(0, n - 1)


    #     self.quickSort(nums, 0, len(nums)-1)
    #     return nums
    

    # def quickSort(self, nums, begin, end):
    #     if begin >= end:
    #         return nums
    #     pivot = self.partition(nums, begin, end)
    #     self.quickSort(nums, begin, pivot-1)
    #     self.quickSort(nums, pivot+1, end)
    
    # def partition(self, nums, begin, end):
    #     pivot = begin
    #     left, right = begin, end 
    #     while left < right:
    #         while left < right and nums[right] > nums[pivot]:
    #             right -= 1
    #         while left < right and nums[left] <= nums[pivot]:
    #             left += 1
    #         nums[left], nums[right] = nums[right], nums[left]
    #     nums[right], nums[pivot] = nums[pivot], nums[right]
    #     return right

        
# @lc code=end


if __name__ == '__main__':
    array = [1,2,3,4, 5,6,7,8,9,10]
    solution = Solution()
    ans = solution.sortArray(array)
    print(ans)