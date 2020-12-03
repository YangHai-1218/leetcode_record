#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_index, end_index =0, len(s)-1
        while start_index < end_index:
            if s[end_index].isalnum() and s[start_index].isalnum():
                if s[start_index].lower() != s[end_index].lower():
                    return False
                start_index += 1
                end_index -= 1
            else:
                if not s[start_index].isalnum():
                    start_index += 1
                if not s[end_index].isalnum():
                    end_index -= 1
        return True

# @lc code=end
s = "8V8K;G;K;V;"
sol = Solution()
print(sol.isPalindrome(s))
