#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start

# version I Time Limit Exceeded
# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         res = []
#         n = len(nums)
#         if not nums:
#             return []
#         for i in range(n-k+1):
#             res.append(max(nums[i:i+k]))
#         return res

# version II
from collections import deque
class Solution:
    
    def maxSlidingWindow(self, nums, k):
        deq = deque()
        res = []
        n = len(nums)
        def clean_deq(i):
            if deq and deq[0] <= i-k:
                deq.popleft()
            
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        def init_deq():
            max_idx = 0
            for i in range(k):
                clean_deq(i)
                deq.append(i)
                if nums[max_idx] < nums[i]:
                    max_idx = i
            res.append(nums[max_idx])

        
        init_deq()
        for i in range(k,n):
            clean_deq(i)
            deq.append(i)
            res.append(nums[deq[0]])
        return res 



# @lc code=end

sol = Solution()
sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)

