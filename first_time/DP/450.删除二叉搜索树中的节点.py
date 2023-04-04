#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self._deletenode(root, key)
    

    def _deletenode(self, node:TreeNode, key:int):
        if node is None:
            return
        
        if node.val == key:
            if node.left is None and node.right is None:
                return None 
            elif node.left is None and node.right is not None:
                return node.right
            elif node.left is not None and node.right is None:
                return node.left
            else:
                cur_node = node.right
                while cur_node.left is not None:
                    cur_node = cur_node.left
                cur_node.left = node.left
                return node.right
        else:
            if node.val < key:
                node.right = self._deletenode(node.right, key)
            else:
                node.left = self._deletenode(node.left, key)
            return node

        
# @lc code=end

