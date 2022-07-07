#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums, m: int) -> int:
        def condition(threshold):
            total = 0
            count = 1
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                if count > m:
                    return False
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left

# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitArray([1,4,4], 3))
