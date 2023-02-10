#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, ans = [root], []
        while queue:
            ans_cur_node = []
            size = len(queue)
            for _ in range(size):
                cur_node = queue.pop(0)
                if cur_node is not None:
                    ans_cur_node.append(cur_node.val)
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            if len(ans_cur_node) > 0:
                ans.append(ans_cur_node)
        return ans[::-1]

# @lc code=end

