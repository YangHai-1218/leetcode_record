#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# stack
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_1, list_2 = [], []
        node = l1
        while node:
            list_1.append(node.val)
            node = node.next

        node = l2
        while node:
            list_2.append(node.val)
            node = node.next

        add = 0
        l_res = None
        while list_1 or list_2:
            num_1 = list_1.pop() if list_1 else 0
            num_2 = list_2.pop() if list_2 else 0
            
            num_3 = num_1 + num_2 + add
            add = 1 if num_3 > 9 else 0
            num_3 = num_3 - add*10
            print(f'num_3:{num_3}, num_2:{num_2}, num_1:{num_1}, add:{add}')
            
            cur_node = ListNode(num_3)
            cur_node.next = l_res
            l_res = cur_node

        if add !=0:
            cur_node = ListNode(add)
            cur_node.next = l_res
            l_res = cur_node
        return l_res
        
# @lc code=end

