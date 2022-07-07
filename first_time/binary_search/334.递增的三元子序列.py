#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         min_num, mid_num = 10000000000000, 10000000000000
#         for num in nums:
#             if num <= min_num:
#                 min_num = num
#             elif num <= mid_num:
#                 mid_num = num
#             elif num > mid_num:
#                 return True
#         return False

class Solution:
    def increasingTriplet(self, nums):
        tail = [nums[0]]
        for num in nums:
            if num > tail[-1]:
                tail.append(num)
                continue
            
            left, right = 0, len(tail)-1
            while left < right:
                mid = left + (right - left)//2
                if tail[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            tail[left] = num
        return len(tail) >= 3
 # @lc code=end

if __name__ == '__main__':
    solution = Solution()
    ans = solution.increasingTriplet([1,2,1,2,1,2,1,2,1,2])
    print(ans)

