#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#


# [x] first time 20-11-09: read other solutions and code by yourself
# [] second time 20-11-09: select the best solution and use cpp to implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# @lc code=start
# class Solution:
#     def merge(self, nums1, m: int, nums2, n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if m == 0:
#             nums1[:] = nums2[:]
#             return
#         if n == 0:
#             return

#         i,j = 0,0
#         nums1_back = nums1.copy()
#         index = 0

#         while i<m and j<n:
#             if nums1_back[i] < nums2[j]:
#                 nums1[index] = nums1_back[i]
#                 i += 1
#             else:
#                 nums1[index] = nums2[j]
#                 j += 1
#             index += 1
#         nums1[index:] = nums1_back[i:m] if i < m else nums2[j:]


# two pointer version
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return
        index = m+n-1
        i,j = m-1,n-1
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        nums1[:index+1] = nums1[:i+1] if i>=0 else nums2[:j+1]

# two pointer version II
# no in-place version
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

# @lc code=end

sol = Solution()
nums1 = [2,0]
sol.merge(nums1,1,[1],1)
print(nums1)


