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

class Solution:
    def levelOrder(self, root: 'Node'):
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            current_level_size = len(queue)
            current_level_nodes = []
            for _ in range(current_level_size):
                current_ndoe = queue.pop(0)
                current_level_nodes.append(current_ndoe.val)
                for child in current_ndoe.children:
                    queue.append(child)
            result.append(current_level_nodes)
        return result
        
# @lc code=end

