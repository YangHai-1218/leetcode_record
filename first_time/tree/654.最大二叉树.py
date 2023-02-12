#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.construct(nums)
        print(root)
        return root

    def construct(self, nums):
        if len(nums) == 0:
            return None
        maxindex = [i for i, n in enumerate(nums) if n==max(nums)][0]
        node = TreeNode(val=nums[maxindex])
        node.left = self.construct(nums[:maxindex])
        if maxindex < len(nums) - 1:
            node.right = self.construct(nums[maxindex+1:])
        return node

# @lc code=end
Solution().constructMaximumBinaryTree([3,2,1,6,0,5])

