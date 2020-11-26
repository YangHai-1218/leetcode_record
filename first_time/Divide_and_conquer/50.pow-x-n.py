#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
# [] first time 20-11-26: read other solutions and code by yourself
# [] second time 20-11-26: select the best solution and use cpp to implement it
# [] third time 20-11-26: after 24 hours
# [] forth time 20-11-26: after a week
# [] fifth time 20-11-26: before interview

# stupid version
# class Solution:
#     def myPow(self, x, n):
#         result = 1
#         if n < 0:
#             x = 1/x
#             n = -n
#         for _ in range(n):
#             result *= x
#         return result

# Divide and conquer version
class Solution:
    def myPow(self, x, n):

        if n < 0:
            x = 1/x
            n = -n
        if n == 1:
            return x
        if n == 0:
            return 1
        
        subresult = self.myPow(x, n//2)
        subresult = subresult * subresult if n % 2 ==0 \
                     else subresult*subresult*x
        return subresult


# @lc code=end

sol = Solution()
print(sol.myPow(0.4458, 0))


