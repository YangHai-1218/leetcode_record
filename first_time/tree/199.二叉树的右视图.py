#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        queue, ans = [root], []
        while queue:
            size = len(queue)
            cur_level_rec = []
            for _ in range(size):
                cur_node = queue.pop(0)
                if cur_node is not None: 
                    cur_level_rec.append(cur_node.val)
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            if len(cur_level_rec) > 0:
                ans.append(cur_level_rec[-1])
        return ans

    

# @lc code=end

