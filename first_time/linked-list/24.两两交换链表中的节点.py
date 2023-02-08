#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(next=head)
        cur, prev = head, dummyhead
        while cur is not None and cur.next is not None:
            prev.next = cur.next
            tmp = cur.next.next 
            cur.next.next = cur 
            cur.next = tmp

            prev = cur 
            cur = tmp
        return dummyhead.next
# @lc code=end

