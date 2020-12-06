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


from collections import defaultdict    
class Solution:
    def isAnagram(self, s, t):
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        for char in s:
            s_freq[char] += 1
        for char in t:
            t_freq[char] += 1
        return s_freq == t_freq   
# @lc code=end

sol = Solution()
print(sol.isAnagram("anagram","nagaram"))
