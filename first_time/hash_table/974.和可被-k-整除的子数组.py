#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dic = defaultdict(list)
        sum_ = 0
        ans = 0
        for num in A:
            sum_ += num
            mod = sum_ % K
            if mod == 0:
                ans += 1
            dic[mod].append(num)
        
        for mod in dic:
            temp =  len(dic[mod])
            ans += temp * (temp-1) / 2
        return int(ans) 
            
        
# @lc code=end

