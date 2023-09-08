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

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         root = ListNode(-1)
#         cur_node = root
#         node_1, node_2 = l1, l2
#         while node_1 is not None and node_2 is not None:
#             if node_1 is None and node_2 is not None:
#                 cur_node.next = node_2
#                 node_2 = node_2.next
#                 cur_node = cur_node.next
#             elif node_1 is not None and node_2 is None:
#                 cur_node.next = node_1
#                 node_1 = node_1.next
#                 cur_node = cur_node.next 
#             else:
#                 if node_1.val < node_2.val:
#                     cur_node.next = node_1
#                     node_1 = node_1.next
#                     cur_node = cur_node.next 
#                 else:
#                     cur_node.next = node_2
#                     node_2 = node_2.next
#                     cur_node = cur_node.next 
#             print(node_1)
#             print(node_2)
#         return root.next



# nums = [1]
# left = 0
# right = len(nums) - 1
# target = 1
# while left <= right:
#     middle = int((left + right)/2)
#     print(f"left_index:{left}, left:{nums[left]}, right_index:{right}, right:{nums[right]}, middle_index:{middle}, middle:{nums[middle]}")
#     if nums[middle] > target:
#         right = middle - 1
#     else:
#         left = middle + 1
# # print(f"final:left_index:{left}, left:{nums[left]}, right_index:{right}, right:{nums[right]}")

# left = 0
# right = len(nums) - 1
# while left <= right:
#     print(f"left_index:{left}, left:{nums[left]}, right_index:{right}, right:{nums[right]}, middle_index:{middle}, middle:{nums[middle]}")
#     middle = int((left + right)/2)
#     if nums[middle] >= target:
#         right = middle - 1
#     else:
#         left = middle + 1
    


# def quicksort(nums, left=None, right=None):
#     def partition(nums, start, end):
#         pivot_index = start
#         pivot = nums[pivot_index]
#         index = pivot_index + 1
#         i = index
#         while i <= end:
#             if nums[i] < pivot:
#                 nums[i], nums[index] = nums[index], nums[i]
#                 index += 1
#             i += 1
#         nums[pivot_index], nums[index-1] = nums[index-1], nums[pivot_index]
#         return index - 1

#     if left is None:
#         left = 0
#     if right is None:
#         right = len(nums) - 1
    
#     if left < right:
#         partition_index = partition(nums, left, right)
#         quicksort(nums, left, partition_index-1)
#         quicksort(nums, partition_index+1, right)
        

class Solution:
    def __init__(self):
        self.result = []
        self.path = []
    def combine(self, n: int, k: int):
        nums = list(range(1, n+1))
        self.dfs(0, k, nums)
        return self.result
    
    def dfs(self, start_index, k, nums):
        if len(self.path) == k:
            self.result.append(self.path.copy())
            return
        for index in range(start_index, len(nums)):
            self.path.append(nums[index])
            self.dfs(index, k, nums)
            self.path.pop(-1)
# Solution().combine(4, 2)
from typing import List

class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(0, nums)
        return self.result


    def backtrack(self, start_index, nums):
        if len(self.path) > 1:
            self.result.append(self.path.copy())
        if start_index >= len(nums):
            return
        
        for index in range(start_index, len(nums)):
            if index != start_index and nums[index-1] == nums[index]:
                continue
            if len(self.path) == 0:
                self.path.append(nums[index])
            elif len(self.path) > 0 and nums[index] >= self.path[-1]:
                self.path.append(nums[index])
            else:
                continue
            self.backtrack(index+1, nums)
            self.path.pop(-1)
print(Solution().findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]))
# quicksort([4, 2, 7, 9, 1, 5, 0])
# print(f"final:left_index:{left}, left:{nums[left]}, right_index:{right}, right:{nums[right]}")