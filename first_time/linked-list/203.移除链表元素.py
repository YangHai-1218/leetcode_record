#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummpyhead = ListNode(next=head)
        node = dummpyhead
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next 
        return dummpyhead.next   
# @lc code=end

