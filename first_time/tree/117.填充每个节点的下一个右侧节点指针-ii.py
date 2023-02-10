#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        while queue:
            size = len(queue)
            cur_level_node = []
            for _ in range(size):
                cur_node = queue.pop(0)
                if cur_node is not None:
                    cur_level_node.append(cur_node)
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            for i in range(len(cur_level_node)-1):
                cur_level_node[i].next = cur_level_node[i+1]
        return root
                

        
# @lc code=end

