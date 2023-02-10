#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
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
    def maxDepth(self, root: 'Node') -> int:
        return self.getdepth(root)
    
    def getdepth(self, node):
        if node is None:
            return 0
        depths = [self.getdepth(c) for c in node.children]
        if len(depths) > 0:
            return max(depths) + 1
        else:
            return 1
        
# @lc code=end

