#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, l1, l2):
        l_3 = ListNode()
        l_res = l_3
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                l_3.next = l1
                l1 = l1.next
            else:
                l_3.next = l2
                l2 = l2.next
            l_3 = l_3.next
        l_3.next = l1 if l1 is not None else l2
        return l_res.next
        
# @lc code=end

sol = Solution()

