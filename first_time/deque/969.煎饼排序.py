#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

# @lc code=start
class Solution:
    def pancakeSort(self, arr):
        ans = []
        left, right = 0, len(arr)-1
        sorted_flag = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                sorted_flag = False
                break
        if sorted_flag:
            return []
        while left < right:
            current_max = float("-inf")
            current_max_index = 0
            for i in range(left, right+1):
                if arr[i] > current_max:
                    current_max = arr[i]
                    current_max_index = i
            if current_max_index == right:
                right -= 1
                continue

            # last flip, to speed up
            if right == 1:
                if arr[left] > arr[right]:
                    ans.append(2)
                break
            
            # first flip: current max value move to first index
            ans.append(current_max_index - left + 1)
            flip_left, flip_right = left, current_max_index
            while flip_left < flip_right:
                arr[flip_left], arr[flip_right] = arr[flip_right], arr[flip_left]
                flip_left += 1
                flip_right -= 1
            
            # second flip, first value and last value switch
            ans.append(right - left + 1)
            flip_left, flip_right = left, right
            while flip_left < flip_right:
                arr[flip_left], arr[flip_right] = arr[flip_right], arr[flip_left]
                flip_left += 1
                flip_right -= 1
            
            right -= 1
            
        return ans

# @lc code=end

arr = [1,2,3]
sol = Solution()
print(sol.pancakeSort(arr))