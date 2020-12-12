#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        record = set()
        n = len(s)
        # 哨兵节点
        s = s+'#'
        for i in range(n):
            s_ = set(s[i])
            for j in range(i+1, n+1):
                if s[j] in s_:
                    break
                s_.add(s[j])
            record.add((i,j))
        ans = 0
        for i,j in record:
            if j-i+1 > ans:
                ans = j-i
        return ans


# @lc code=end

sol = Solution()
print(sol.lengthOfLongestSubstring("au"))