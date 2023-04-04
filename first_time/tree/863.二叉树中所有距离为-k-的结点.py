#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
class Solution:
    def __init__(self) -> None:
        self.results = []
        self.parents = dict()
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.findparents(root)
        self.traversal(target, None, K, 0)
        return self.results
    
    def findparents(self, node:True):
        if node.left is not None:
            self.parents[node.left.val] = node 
            self.findparents(node.left)
        if node.right is not None:
            self.parents[node.right.val] = node 
            self.findparents(node.right)

    def traversal(self, node:TreeNode, from_node:TreeNode, K:int, distance:int):
        if distance == K:
            self.results.append(node.val)
            return
        if node.val in self.parents and self.parents[node.val] is not from_node:
            self.traversal(self.parents[node.val], node, K, distance+1)
        if node.left is not None and node.left is not from_node:
            self.traversal(node.left, node, K, distance+1)
        if node.right is not None and node.right is not from_node:
            self.traversal(node.right, node, K, distance+1)
        




        
# @lc code=end

