#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return s
        start_index, end_index = 0, len(s)-1
        while start_index < end_index:
            s[start_index], s[end_index] = s[end_index], s[start_index]
            start_index += 1
            end_index -= 1
# @lc code=end

