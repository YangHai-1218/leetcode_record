#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# [x] first time 20-12-01: read other solutions and code by yourself
# [x] second time 20-12-01: select the best solution and use cpp to implement it
# [] third time 20-12-01: after 24 hours
# [] forth time 20-12-01: after a week
# [] fifth time 20-12-01: before interview
# @lc code=start
# class Solution:
#     def coinChange(self, coins, amount):
#         if amount == 0:
#             return 0
#         self.coins = coins
#         self.coin_num = len(coins)
#         self.result = []
#         self._coinChange(amount, 0)
#         if not self.result:
#             return -1
#         else:
#             return min(self.result)
#     def _coinChange(self, amount, counts):
#         for i in range(self.coin_num):
#             if amount - self.coins[i] == 0:
#                 self.result.append(counts + 1)
#             if i == 0 and amount - self.coins[i] < 0:
#                 return
#         for i in range(self.coin_num):
#             self._coinChange(amount-self.coins[i], counts + 1)

# https://www.bilibili.com/video/BV16Y411v7Y6/?vd_source=ef160799f07d4a29c559b2c10a4bb26b
class Solution:
    def coinChange(self, coins, amount):
        dp = [[10000000 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount+1):
                if c < x:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = min(dp[i][c], dp[i+1][c-x]+1)
        return dp[-1][-1] if dp[-1][-1] < 10000000 else -1

# class Solution:
#     def coinChange(self, coins, amount):
#         ans = self.dfs(len(coins)-1, amount, coins)
#         return ans if ans < 10000000 else -1

#     def dfs(self, i, c, coins):
#         if i < 0:
#             return 0 if c == 0 else 10000000
#         if c < coins[i]:
#             return self.dfs(i-1, c, coins)
#         return min(self.dfs(i-1, c, coins), self.dfs(i, c-coins[i], coins)+1)
# @lc code=end

sol = Solution()
print(sol.coinChange([1,2,5],11))

