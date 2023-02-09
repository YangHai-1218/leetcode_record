#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def getsum(self, n):
        sum = 0
        while n:
            sum += (n%10) * (n%10)
            n = n//10
        return sum
    def isHappy(self, n: int) -> bool:
        record = set()
        while True:
            n = self.getsum(n)
            if n in record:
                return False 
            elif n == 1:
                return True 
            else:
                record.add(n)
        

# @lc code=end
Solution().isHappy(19)

