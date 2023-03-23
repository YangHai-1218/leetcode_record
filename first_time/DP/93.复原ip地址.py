#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s):
        self.ans = []
        self.dfs(s, 0, "")
        return self.ans
        
    def dfs(self, s, index, path):
        if index > 4:
            return
        if index == 4 and not s:
            self.ans.append(path[:-1])
            return 
        for i in range(1, len(s)+1):
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:],index+1, path+s[:i]+'.')

# @lc code=end

sol = Solution()
print(sol.restoreIpAddresses("010010"))
