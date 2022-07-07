#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start


# It's so hard
# https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False]*(1+n) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(n):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1] = True
        for i in range(m):
            for j in range(n):
                if p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] != '*':
                    if p[j] == s[i]:
                        dp[i+1][j+1] = dp[i][j]
                    else:
                        dp[i+1][j+1] = False
                else:
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j] or dp[i+1][j-1] or dp[i][j+1]      
        return dp[-1][-1]


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    ans = solution.isMatch("aab", "c*a*b")
    print(ans)

