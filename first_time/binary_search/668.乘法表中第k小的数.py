#
# @lc app=leetcode.cn id=668 lang=python3
#
# [668] 乘法表中第k小的数
#

# @lc code=start
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def condition(num):
            less_than_num = 0
            for j in range(1, m+1):
                add = min(num // j, n)
                less_than_num += add
                if add == 0:
                    break
            return less_than_num >= k

        left, right = 1, m*n
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right  = mid
            else:
                left = mid + 1
        return left
        
# @lc code=end

