#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursion version
# class Solution:
#     def __init__(self):
#         self.traverse_path_list = []

#     def levelOrder(self, root):
#         if root is None:
#             return []
#         self.traverse_path_list.append([root.val])
#         if root.children:
#             self.levelOrder_(root.children)
#         return self.traverse_path_list
    
#     def levelOrder_(self,children):
#         list_children = []
#         temp_list = []
#         for child in children:
#             temp_list.append(child.val)
#             list_children.extend(child.children)
#         self.traverse_path_list.append(temp_list)
#         if not list_children:
#             return 
#         self.levelOrder_(list_children)

# loop version
from collections import deque
class Solution:
    def __init__(self):
        self.traverse_path_list = []

    def levelOrder(self, root):
        if not root:
            return []
        deq = deque([root])
        while deq:
            level = []
            len_deq = len(deq)
            for _ in range(len_deq):
                node = deq.popleft()
                level.append(node.val)
                deq.extend(node.children)
            self.traverse_path_list.append(level)
        return self.traverse_path_list
    
        
        
# @lc code=end



