#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from typing import List
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        record = [0 for _ in range(26)]
        for c in p:
            record[ord(c) - ord('a')] += 1
        
        res = []
        for i in range(len(s) - len(p) + 1):
            # initialize record
            if i == 0:
                for j in range(len(p)):
                    record[ord(s[i+j]) - ord('a')] -= 1
            else:
                record[ord(s[i-1]) - ord('a')] += 1
                record[ord(s[i+len(p)-1]) - ord('a')] -= 1
            if all(r==0 for r in record):
                res.append(i)
        return res

# @lc code=end
print(Solution().findAnagrams("abab", "ab"))

