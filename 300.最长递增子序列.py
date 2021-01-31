#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
# dp version
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [1] * len(nums)
#         for i, num in enumerate(nums):
#             if i== 0:
#                 continue          
#             dp[i] = max([0] + [dp[j] for j in range(i) if nums[j] < num])
#             dp[i] += 1
#         return max(dp)

# greedy + binary search version
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        
        for num in nums:
            if num > tail[-1]:
                tail.append(num)
                continue
            
            left, right = 0, len(tail)-1
            while left < right:
                mid = (left + right)//2
                if nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            nums[left] = num
        return len(tail)             
# @lc code=end

