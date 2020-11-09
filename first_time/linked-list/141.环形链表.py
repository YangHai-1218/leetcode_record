#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# [x] first time 20-11-09: read other solutions and code by yourself
# [] second time 20-11-09: select the best solution and use cpp to implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview


class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        passed_node = {}
        node = head
        while node.next is not None:
            if node in passed_node:
                return True
            passed_node[node] = node.val
            node = node.next
        return False
# @lc code=end




