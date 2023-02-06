#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#



#范围查询规律
#初始化:
#  int left = 0;
#  int right = nums.length - 1;
#循环条件
#  left <= right
#右边取值
#  right = mid - 1
#左边取值
#  left = mid + 1
#查询条件
#  >= target值, 则 nums[mid] >= target时, 都减right = mid - 1
#  >  target值, 则 nums[mid] >  target时, 都减right = mid - 1
#  <= target值, 则 nums[mid] <= target时, 都加left = mid + 1
#  <  target值, 则 nums[mid] <  target时, 都加left = mid + 1
#结果
#  求大于(含等于), 返回left
#  求小于(含等于), 返回right
#核心思想: 要找某个值, 则查找时遇到该值时, 当前指针(例如right指针)要错过它, 让另外一个指针(left指针)跨过他(体现在left <= right中的=号), 则找到了


# @lc code=start
class Solution:
    def searchRange(self, nums:list, target:int):
        leftindex = self.binary_searach(nums, target)
        # leftindex > len(nums) - 1, 则list中所有元素比target小
        # nums[leftindex] != target， 则list中不存在target
        if leftindex > len(nums) - 1 or nums[leftindex] != target:
            return [-1, -1]
        rightindex = self.binary_searach(nums, target+1)
        return [leftindex, rightindex-1]
        


    def binary_searach(self, nums:list, target:int):
        # 找到第一个>=target的index
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

# @lc code=end
sol = Solution()
print(sol.searchRange([1],1))
