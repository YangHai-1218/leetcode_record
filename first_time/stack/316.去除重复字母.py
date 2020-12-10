#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start

"https://leetcode-cn.com/problems/remove-duplicate-letters/solution/you-qian-ru-shen-dan-diao-zhan-si-lu-qu-chu-zhong-/"
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        instack = set()
        count = dict(Counter(s))
        for char in s:
            count[char] -= 1
            if char in instack:
                continue
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                instack.remove(stack.pop())
            stack.append(char)
            instack.add(char)
        ans = []
        while stack:
            ans.append(stack.pop(0))
        return "".join(ans)
        

# @lc code=end

sol = Solution()
print(sol.removeDuplicateLetters("bbcaac"))