#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.traverse_path_list = []
    def preorder_(self, root):
        if not root:
            return
        self.traverse_path_list.append(root.val)
        for node in root.children:
            self.preorder_(node)
    def preorder(self,root):
        self.preorder_(root)
        return self.traverse_path_list

        
# @lc code=end

