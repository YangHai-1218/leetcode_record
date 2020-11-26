#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# [x] first time 20-11-11: read other solutions and code by yourself
# [] second time 20-11-11: select the best solution and use cpp to implement it
# [] third time 20-11-11: after 24 hours
# [] forth time 20-11-11: after a week
# [] fifth time 20-11-11: before interview
# @lc code=start
import collections
class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []
        chars = {}
        for i,char in enumerate('abcdefghijklmnopqrstuvwxyz'):
            chars[char] = i
        res = collections.defaultdict(list)
        for str_ in strs:
            count = [0 for i in range(26)]
            for char in str_:
                count[chars[char]] += 1
            res[tuple(count)].append(str_)
        return list(res.values())
# @lc code=end

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

