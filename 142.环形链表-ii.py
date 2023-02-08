#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_node, fast_node = head, head 
        cycle_flag = False 
        while slow_node is not None:
            if fast_node == slow_node:
                
            if fast_node.next is None:
                break
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            
        
# @lc code=end

