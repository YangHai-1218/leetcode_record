#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
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
    def postorder_(self, root):
        if not root:
            return
        for node in root.children:
            self.postorder_(node)
        self.traverse_path_list.append(root.val)
    def postorder(self,root):
        self.postorder_(root)
        return self.traverse_path_list
        
# @lc code=end

