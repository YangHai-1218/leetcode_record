#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有 K 个重复字符的最长子串
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self._longersubstring(s, k)

    def _longersubstring(self, s:str, k:int):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self._longersubstring(sub_str, k) for sub_str in s.split(c))
        return len(s)
# @lc code=end

