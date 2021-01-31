#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
import math
class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        def condition(speed):
            return sum([math.ceil(pile/speed) for pile in piles]) <= H
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
                
                    
# @lc code=end

if __name__== '__main__':
    piles = [3,6,7,11]
    solution = Solution()
    print(solution.minEatingSpeed(piles, 8))

