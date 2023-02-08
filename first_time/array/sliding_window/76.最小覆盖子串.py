#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

from collections import defaultdict
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        leftindex, rightindex = 0, 0
        result = 1000000
        result_leftindex, result_rightindex = 0, 0
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        while rightindex < len(s):
            if s[rightindex] in t_count:
                t_count[s[rightindex]] -= 1
            while all(c <= 0 for c in t_count.values()):
                sub_len = rightindex - leftindex + 1
                if sub_len < result:
                    result = sub_len
                    result_leftindex = leftindex
                    result_rightindex = rightindex
                if s[leftindex] in t_count:
                    t_count[s[leftindex]] += 1
                leftindex += 1
            rightindex += 1
        return s[result_leftindex:result_rightindex+1] if result != 1000000 else ""
# @lc code=end
print(Solution().minWindow("ab", "a"))
