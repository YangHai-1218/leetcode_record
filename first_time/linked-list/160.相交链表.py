#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a, len_b = 0, 0
        cur = headA
        while cur is not None:
            cur = cur.next
            len_a += 1

        cur = headB
        while cur is not None:
            cur = cur.next
            len_b += 1
        
        fast_head = headA if len_a > len_b else headB
        slow_head = headA if len_a <= len_b else headB
        cur_fast, cur_slow = fast_head, slow_head
        diff_len = abs(len_a - len_b)
        while diff_len > 0:
            cur_fast = cur_fast.next
            diff_len -= 1
        
        while cur_slow is not None and cur_fast is not None:
            if cur_fast == cur_slow:
                return cur_fast
            else:
                cur_fast = cur_fast.next
                cur_slow = cur_slow.next
        return None


        
# @lc code=end

