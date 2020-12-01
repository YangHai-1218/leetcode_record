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


class Solution:
    def coinChange(self, coins, amount):
        change_nums = [amount + 1] * (amount+1)
        change_nums[0] = 0
        for i in range(1, amount+1):
            for k in range(len(coins)):
                if coins[k] > i:
                    continue
                change_nums[i] = min(change_nums[i], change_nums[i-coins[k]] + 1)
        return -1 if change_nums[-1]==amount+1 else change_nums[-1]
# @lc code=end

sol = Solution()
print(sol.coinChange([1,2,5],11))

