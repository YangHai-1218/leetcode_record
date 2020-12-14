#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next, slow.next
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)
        res = ListNode(-1)
        h = res
        while left and right:
            if left.val < right.val :
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left or right
        return res.next
            

# @lc code=end

root = ListNode(4)
root.next = ListNode(2)
root.next.next = ListNode(1)
root.next.next.next = ListNode(3)
sol = Solution()
print(sol.sortList(root))