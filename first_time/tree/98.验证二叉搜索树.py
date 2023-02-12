#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None or root.right is None:
            return True
        leftmaxval, leftminval = self.getmaxmin(root.left)
        if leftmaxval is False or leftminval is False:
            return False
        rightmaxval, rightminval = self.getmaxmin(root.right)
        if rightmaxval is False or rightminval is False:
            return False 
        if root.val > leftmaxval and root.val < rightminval:
            return True
        else:
            return False
    

    def getmaxmin(self, node):
        if node.left is None and node.right is None:
            return node.val, node.val
        
        
        if node.left is not None:
            leftmaxval, leftminval = self.getmaxmin(node.left)
            if leftmaxval is False and leftminval is False:
                return False
        
        if node.right is not None:
            rightmaxval, rightminval = self.getmaxmin(node.right)
            if rightminval is False and rightmaxval is False:
                return False

        
        if leftmaxval < node.val and rightminval > node.val:
            return max(leftmaxval, rightmaxval), min(leftminval, rightminval)
        else:
            return False, False

        

# @lc code=end

root  = TreeNode(5)
a = TreeNode(4)
b = TreeNode(6)
c = TreeNode(3)
d = TreeNode(7)
root.left = a
root.right = b
b.left = c
b.right = d
sol = Solution()
print(sol.isValidBST(root))

