#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        if len(nums) == 1:
            return [[nums.pop()], [ ]]
        

        current_value = nums.pop()
        subresult = self.subsets(nums)
        subresult_ = subresult.copy()
        for l in subresult_:
            l_ = l.copy()
            l_.append(current_value)
            subresult.append(l_)
        return subresult

        

# @lc code=end
sol = Solution()
print(sol.subsets([1,2,3]))
