#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode/
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n or not head:
            return head
        
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m-1, n-1

        tail, con = cur, prev
        while n:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
            n -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head

        
# @lc code=end


sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = sol.reverseBetween(head, 2, 4)
node = head
while node:
    print(node.val)
    node = node.next