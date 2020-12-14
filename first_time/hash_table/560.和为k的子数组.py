#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
# 前缀和
from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k) -> int:

        sum_ = 0
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0
        for num in nums:
            sum_ += num
            if sum_ - k in dic:
                ans += dic[sum_ - k]
            dic[sum_] += 1
        
        return ans


# @lc code=end

sol = Solution()
sol.subarraySum([1,1,1],2)