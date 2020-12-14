#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_1, node_2 = l1, l2
        root = ListNode(-1)
        node = root
        add = 0
        while node_1 or node_2:
            num_1 = node_1.val if node_1 else 0
            num_2 = node_2.val if node_2 else 0
            num_3 = num_1 + num_2 + add 
            add = 1 if num_3 > 9 else 0
            num_3 = num_3 - add*10
            node.val = num_3

            prev_node = node
            next_node = ListNode(-1)
            node.next = next_node
            node = next_node

            node_1 = node_1.next if node_1 else None
            node_2 = node_2.next if node_2 else None
        if add != 0:
            node.val = add
        else:
            prev_node.next = None
        return root


            
        
# @lc code=end

root_1 = ListNode(9)
root_1.next = ListNode(9)
root_1.next.next = ListNode(9)
root_2 = ListNode(9)
root_2.next = ListNode(9)

sol = Solution()
print(sol.addTwoNumbers(root_1, root_2))