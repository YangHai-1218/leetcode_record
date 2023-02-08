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
        prev, node = None, head 
        while node is not None:
            tmp = node.next
            node.next = prev
            prev = node 
            node = tmp
        return prev
            
        

# @lc code=end
head = ListNode(1)
head2 = ListNode(2)
head.next = head2
sol = Solution()
cur = sol.reverseList(head)

while cur:
    print(cur.val)
    cur = cur.next


