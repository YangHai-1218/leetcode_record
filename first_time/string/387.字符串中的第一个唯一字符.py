#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
        for i,char in enumerate(s):
            if dic[char] == 1:
                return i
        return -1

# @lc code=end
sol = Solution()
print(sol.firstUniqChar("leetcode"))

