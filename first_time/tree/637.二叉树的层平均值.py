#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue, ans = [root], []
        while queue:
            size = len(queue)
            ans_cur_level = []
            for _ in range(size):
                cur_node = queue.pop(0)
                if cur_node is not None:
                    ans_cur_level.append(cur_node.val)
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            if len(ans_cur_level) > 0:
                ans.append(sum(ans_cur_level)/len(ans_cur_level))
        return ans
# @lc code=end

