# def swap(input_list, i, j):
#     input_list[i], input_list[j] = input_list[j], input_list[i]

# def partiton(input_list, left, right):
#     i = left - 1
#     pivot = input_list[right]

#     for j in range(left, right):
#         if input_list[j] <= pivot:
#             i = i+1
#             swap(input_list, i, j)
    
#     swap(input_list, i+1, right)
#     return i+1


# def quicksort(input_list, left, right):
#     if left < right:
#         pi = partiton(input_list, left, right)
#         quicksort(input_list, left, pi-1)
#         quicksort(input_list, pi+1, right)

# input_list = [2, 1, 3, 5, 7, 8, 6, 4]
# quicksort(input_list, 0, len(input_list)-1)
# print(input_list)




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(-1)
        cur_node = root
        node_1, node_2 = l1, l2
        while node_1 is not None and node_2 is not None:
            if node_1 is None and node_2 is not None:
                cur_node.next = node_2
                node_2 = node_2.next
                cur_node = cur_node.next
            elif node_1 is not None and node_2 is None:
                cur_node.next = node_1
                node_1 = node_1.next
                cur_node = cur_node.next 
            else:
                if node_1.val < node_2.val:
                    cur_node.next = node_1
                    node_1 = node_1.next
                    cur_node = cur_node.next 
                else:
                    cur_node.next = node_2
                    node_2 = node_2.next
                    cur_node = cur_node.next 
            print(node_1)
            print(node_2)
        return root.next

