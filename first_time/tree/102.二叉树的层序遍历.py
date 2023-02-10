#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS version
class Solution:
    def levelOrder(self, root):
        result = []
        self.Order(0, result, root)
        return result
        
    def Order(self, depth, result, node):
        if node is None:
            return
        if depth == len(result):
            result.append([])
        result[depth].append(node.val)
        self.Order(depth+1, result, node.left)
        self.Order(depth+1, result, node.right)

        
        
# BFS version
# class Solution:
#     def levelOrder(self, root):
#         queue, ans = [root, ], []
#         while queue:
#             size = len(queue)
#             ans_cur_level = []
#             for _ in range(size):
#                 cur_node = queue.pop(0)
#                 if cur_node is not None:
#                     ans_cur_level.append(cur_node.val)
#                     queue.append(cur_node.left)
#                     queue.append(cur_node.right)
#             if len(ans_cur_level) > 0:
#                 ans.append(ans_cur_level)
#         return ans




# @lc code=end
root = TreeNode(10)
depth_1 = TreeNode(20)
depth_2 = TreeNode(30)
root.left, root.right = depth_1, depth_2
sol = Solution()
print(sol.levelOrder(root))

