#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#

# @lc code=start
import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def condition(num):
            count = num // a + num // b + num // c  - num // ac - num // bc  - num//ab + num//abc
            return count >= n
        
        ab = a * b // math.gcd(a,b)
        bc = b * c // math.gcd(b, c)
        ac = a * c // math.gcd(a, c)
        abc = a * bc // math.gcd(a, bc)

        left, right = 1, 10**10
        while left < right:
            mid = left + (right - left)//2
            if condition(mid):
                right = mid
            else:
                left = mid +1

        return left
# @lc code=end

