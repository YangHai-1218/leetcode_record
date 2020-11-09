#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start


# stupid version 
# result:
# Your runtime beats 13.34 % of python3 submissions(64 ms)
# Your memory usage beats 11.92 % of python3 submissions (13.7 MB)
# class Solution:
#     def strStr(self, haystack, needle):
#         if not needle:
#             return 0
#         head_needle = needle[0]
#         len_needle = len(needle)
#         for i, r in enumerate(haystack):
#             if r == head_needle:
#                 if haystack[i:i+len_needle] == needle:
#                     return i
#         return -1

# call libaray function
# result:
#   Your runtime beats 92.96 % of python3 submissions(36 ms)
#   Your memory usage beats 13.72 % of python3 submissions (13.7 MB)
class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        return haystack.find(needle)

# kmp algorithm solution



# @lc code=end

solution = Solution()
answer = solution.strStr('hello', 'll')
print(answer)