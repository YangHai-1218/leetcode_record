# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pointer_1, pointer_2 = l1, l2
        cur_node = ListNode(0)
        dummpy_node = cur_node
        while pointer_1 and pointer_2:
            if pointer_1.val < pointer_2.val:
                cur_node.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                cur_node.next = pointer_2
                pointer_2 = pointer_2.next
        cur_node.next = pointer_1 if pointer_1 else pointer_2
        return dummpy_node.next
