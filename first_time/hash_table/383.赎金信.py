#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0 for _ in range(26)]
        for c in magazine:
            record[ord(c) - ord('a')] += 1
        for c in ransomNote:
            index = ord(c) - ord('a')
            record[index] -= 1
            if record[index] < 0:
                return False
        return True
# @lc code=end

