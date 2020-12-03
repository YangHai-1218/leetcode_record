#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_ = s.split(' ')
        index = len(s_) -1
        s = s_[index]
        while s=='' and index >=0:
            index -= 1
            s = s_[index]
        return len(s) if s!='' else 0

# @lc code=end
s = "        "
sol = Solution()
print(sol.lengthOfLastWord(s))
