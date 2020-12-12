#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
# https://leetcode-cn.com/problems/next-greater-element-i/solution/xia-yi-ge-geng-da-yuan-su-i-by-leetcode/
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # 单调栈
        stack = []
        dic = dict()
        for i in range(len(nums2)-1, -1, -1): # 倒着入栈
            while stack and nums2[i] > stack[-1]: # 将后边所有比当前这个人个子矮的pop，因为当前这个人是看不到这些矮个子的
                stack.pop()
            dic[nums2[i]] =  -1 if not stack else stack[-1] # 此时当前这个人可以看到的就是栈顶元素，如果栈空了，说明当前这个人后面没有更高的人了
            stack.append(nums2[i]) # 将当前这个人入栈
        ans = []
        for num in nums1:
            ans.append(dic[num])
        return ans

        
# @lc code=end

sol = Solution()
print(sol.nextGreaterElement([2,4], [1,2,3,4]))
