#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):    
        list_len = 0
        node = head
        while node is not None:
            list_len += 1
            node = node.next
        head_ = ListNode(0)
        head_.next = head
        index = 0
        target_index = list_len - n
        node = head_
        while index <= target_index-1:
            node = node.next
            index += 1
        node.next = node.next.next
        return head_.next


        
# @lc code=end
a  = ListNode(1)
b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
a.next = b
# b.next = c
# c.next = d
# d.next = e
sol = Solution()
print(sol.removeNthFromEnd(a, 2))

