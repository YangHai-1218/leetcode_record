#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        n = len(nums)
        ans = [-1] * n
        for i in range(2*n-1, -1, -1):
            while stack and nums[i%n] >= stack[-1]:
                stack.pop()
            ans[i%n] = -1 if not stack else stack[-1]
            stack.append(nums[i%n])
        return ans
            

                   
# @lc code=end

nums = [1,2,1]
sol = Solution()
print(sol.nextGreaterElements(nums))