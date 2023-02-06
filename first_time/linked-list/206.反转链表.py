#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for single-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        prev, cur = head, None
        while True:
            cur = head.next
            head.next = cur.next
            cur.next = prev
            if head.next is None:
                return cur
            prev = cur
            
        

# @lc code=end
head = ListNode(1)
head2 = ListNode(2)
head.next = head2
sol = Solution()
cur = sol.reverseList(head)

while cur:
    print(cur.val)
    cur = cur.next


