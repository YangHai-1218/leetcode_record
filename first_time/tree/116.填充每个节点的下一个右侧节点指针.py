#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         queue = [root]
#         while queue:
#             size = len(queue)
#             record_per_level = []
#             for _ in range(size):
#                 cur_node = queue.pop(0)
#                 if cur_node is not None:
#                     record_per_level.append(cur_node)
#                     queue.append(cur_node.left)
#                     queue.append(cur_node.right)
#             if len(record_per_level)>0:
#                 for i in range(len(record_per_level)-1):
#                     record_per_level[i].next = record_per_level[i+1]
#         return root


# 完美二叉树
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        if root.left is None:
            return root
        else:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root       
# @lc code=end

