#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
# 模拟加法的进位
class Solution:
    def addStrings(self, num1, num2):
        ans = ''
        add = 0
        i, j =len(num1)-1 , len(num2)-1
        while i >=0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            if n1 + n2 + add >= 10:
                ans = str(n1+n2+add-10) + ans
                add = 1
            else:
                ans = str(n1+n2+add) + ans
                add = 0
            i -= 1
            j -= 1
        if add == 1:
            ans = '1' + ans
        return ans
        
# @lc code=end

sol = Solution()
print(sol.addStrings("1","1"))
