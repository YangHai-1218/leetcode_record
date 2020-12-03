#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        set_j = set(J)
        result = 0
        for s in S:
            if s in set_j:
                result += 1
        return result

        
# @lc code=end

