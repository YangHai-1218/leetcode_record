#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
# class Solution:
#     def fib(self, N):
#         if N <= 0:
#             return 0
#         elif N<=1:
#             return 1
#         else:
#             return self.fib(N-1) + self.fib(N-2)

# bottom up version
class Solution:
    def fib(self, N):
        memo = [0 for i in range(N+1)]
        return self._fib(N, memo)

    def _fib(self, n, memo):
        if n <= 1:
            return n
        if memo[n] == 0:
            memo[n] = self._fib(n-1, memo) + self._fib(n-2, memo)
        return memo[n]



        
# @lc code=end

sol = Solution()
print(sol.fib(0))