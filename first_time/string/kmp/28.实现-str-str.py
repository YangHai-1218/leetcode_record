#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start




# call libaray function
# class Solution:
#     def strStr(self, haystack, needle):
#         if not needle:
#             return 0
#         return haystack.find(needle)

# kmp algorithm solution
class Solution:
    def strStr(self, haystack, needle):
        next = self.getNext(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and needle[j] != haystack[i]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


    def getNext(self, needle):
        j= 0 
        next_ = [0 for _ in range(len(needle))]
        # i:后缀 j:前缀
        for i in range(1, len(needle)):
            while j > 0 and needle[j] != needle[i]:
                j = next_[j-1]
            if needle[j] == needle[i]:
                j += 1
            next_[i] = j 
        return next_




# @lc code=end

solution = Solution()
answer = solution.strStr('hello', 'll')
print(answer)