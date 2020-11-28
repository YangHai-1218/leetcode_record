#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num):
        x_old, C = float(num), float(num)
        while True:
            x_new = (x_old + C/x_old)/2
            if abs(x_new - x_old) < 1e-6:
                break
            x_old = x_new
        if abs(x_new - int(x_new)) < 1e-6 or abs(x_new-int(x_new)-1) < 1e-6:
            return True
        else:
            return False

# @lc code=end

