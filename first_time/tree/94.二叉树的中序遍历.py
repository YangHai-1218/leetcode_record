#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.traverse_path_list = []
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.traverse_path_list.append(root.val)
        self.inorder(root.right) 
    def inorderTraversal(self,root):
        self.inorder(root)
        return self.traverse_path_list
# @lc code=end

root = TreeNode(val=1)
right = TreeNode(val=2)
left = TreeNode(val=3)
root.right = right
right.left = left

sol = Solution()
sol.inorderTraversal(root)
