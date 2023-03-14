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
        root = self.construct(nums, 0, len(nums)-1)
        print(root)
        return root

    def construct(self, nums, left, right):
        if left > right:
            return None
        nums_ = nums[left:right+1]
        maxindex = [i for i, n in enumerate(nums_) if n == max(nums_)][0] + left
        node = TreeNode(val=nums[maxindex])
        node.left = self.construct(nums, left, maxindex-1)
        node.right = self.construct(nums, maxindex+1, right)
        return node

# @lc code=end
Solution().constructMaximumBinaryTree([3,2,1,6,0,5])

