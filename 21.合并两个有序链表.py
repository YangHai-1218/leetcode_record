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
# solution for list version
class Solution:
    def mergeTwoLists(self, l1, l2):
        max_l_index = 0
        merged_list = []
        print(l1, l2)
        l_min, l_max = (l1, l2) if l1[0]<l2[0] else (l2, l1)
        len_min, len_max = len(l_min), len(l_max)

        for i, l_min_num in enumerate(l_min):
            merged_list.append(l_min_num)
            
            if i < len_min - 1:
                for _ in range(max_l_index, len_max):
                    l_max_num = l_max[max_l_index]
                    if l_max_num < l_min[i+1]:
                        merged_list.append(l_max_num)
                        max_l_index += 1
                    else:
                        break
        
        merged_list.extend(l_max[max_l_index:])
        return merged_list

class Solution:
    def mergeTwoLists(self, l1, l2):
        mergeed_list = []
        if l1.val < l2.val:
            mergeed_list.append(l1.val)
        else:
            mergeed_list.append(l2.val)
        if l1.next is None and l2.next is None:
            return mergeed_list
        elif l1.next is None and l2.next is not None:
            return 
# @lc code=end

solution = Solution()
print(solution.mergeTwoLists([1,2,4], [1,3,4]))
