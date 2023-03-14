#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.construct_subtree(nums, 0, len(nums)-1)
        
    def construct_subtree(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(val = nums[mid])
        node.left = self.construct_subtree(nums, left, mid-1)
        node.right = self.construct_subtree(nums, mid+1, right)
        return node
        
# @lc code=end
Solution().sortedArrayToBST([-10,-3,0,5,9])

