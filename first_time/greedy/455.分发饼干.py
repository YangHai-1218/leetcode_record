#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        result = 0
        for g_i in g:
            for s_i in s:
                if s_i >= g_i:
                    result += 1
                    s.remove(s_i)
                    break
        return result
# @lc code=end
sol = Solution()
print(sol.findContentChildren([1,2], [1,2,3]))

