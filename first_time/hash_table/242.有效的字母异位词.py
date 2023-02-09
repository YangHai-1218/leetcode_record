#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# [x] first time 20-11-11: read other solutions and code by yourself
# [] second time 20-11-11: select the best solution and use cpp to implement it
# [] third time 20-11-11: after 24 hours
# [] forth time 20-11-11: after a week
# [] fifth time 20-11-11: before interview
# @lc code=start


# class Solution:
#     def isAnagram(self, s, t):
#         t_freq = {}
#         s_freq = {}
#         for char in s:
#             if char in s_freq:
#                 s_freq[char] += 1
#             else:
#                 s_freq[char] = 1
#         for char in t:
#             if char in t_freq:
#                 t_freq[char] += 1
#             else:
#                 t_freq[char] = 1
#         if s_freq == t_freq:
#             return True
#         else:
#             return False  

class Solution:
    def isAnagram(self, s, t):
        record = [0 for _ in range(26)]
        for c in s:
            record[ord(c)-ord('a')] += 1
        for c in t:
            record[ord(c)-ord('a')] -= 1
        
        return all(t==0 for t in record)
# @lc code=end

sol = Solution()
print(sol.isAnagram("anagram","nagaram"))
