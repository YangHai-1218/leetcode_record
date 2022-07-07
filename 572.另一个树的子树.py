#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.identical(s, t):
            return True
        # if s is None and t is None, then they will be identical
        # if here, means s is None, but t is not None, return False
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    
    def identical(self, s, t):
        # if s is None or t is None
        if not (s and t):
            return s is t
        
        return s.val == t.val and \
                self.identical(s.left, t.left) and \
                self.identical(s.right, t.right)
    

        
       

        
# @lc code=end

