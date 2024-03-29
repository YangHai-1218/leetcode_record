#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.result = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        self.traversal(root, path)
        return self.result

    def to_string(self, path):
        string = ''
        for i in range(len(path)-1):
            string += str(path[i]) + '->'
        string += str(path[-1])
        return string


    def traversal(self, node, path:List):
        path.append(node.val)
        if node.left is None and node.right is None:
            self.result.append(self.to_string(path))
            return
        
        if node.left is not None:
            self.traversal(node.left, path, self.result)
            path.pop(-1)
        
        if node.right is not None:
            self.traversal(node.right, path, self.result)
            path.pop(-1)
        return
            
# @lc code=end

