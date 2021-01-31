#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def condition(capacity):
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    days += 1
                if days > D:
                    return False
            return True
        
        left, right  = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end

