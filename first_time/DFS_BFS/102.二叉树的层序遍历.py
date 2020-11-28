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
# class Solution:
#     def levelOrder(self, root):
#         if root is None:
#             return []
#         result = [[]]
#         return self._levelOrder(level=1,result=result,node=root)
        
#     def _levelOrder(self, level, result, node):
#         if node is None:
#             return
#         result[level-1].append(node.val)
#         left_node, right_node = node.left, node.right
#         if left_node is None and right_node is None:
#             self._levelOrder(level+1, result, left_node)
#         else:
#             if len(result) < (level +1 ):
#                 result.append([])
#             self._levelOrder(level+1, result, left_node)
#             self._levelOrder(level+1, result, right_node)
#         return result
        
# BFS version
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            current_level_size = len(queue)
            result.append([])
            for _ in range(current_level_size):
                current_node = queue.pop(0)
                result[-1].append(current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
        return result


# @lc code=end
root = TreeNode(10)
depth_1 = TreeNode(20)
depth_2 = TreeNode(30)
root.left, root.right = depth_1, depth_2
sol = Solution()
print(sol.levelOrder(root))

