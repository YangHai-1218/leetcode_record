#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#

# @lc code=start
# 先计算出对于每个元素来说，它之前所有所有元素的最小值
# 之后按照下一个更大元素的思路
class Solution:
    def find132pattern(self, nums):
        min_stack = []
        for num in nums:
            if not min_stack:
                min_stack.append(num)
            else:
                min_stack.append(min(num, min_stack[-1]))
        print(min_stack)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if min_stack[i] < nums[i]:
                while stack and min_stack[i] >= nums[stack[-1]]:
                    stack.pop()
                if stack and nums[i] > nums[stack[-1]]:
                    return True
                stack.append(i)
        return False

# @lc code=end
sol = Solution()
print(sol.find132pattern([2,3,1,2]))
