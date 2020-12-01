#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# [x] first time 20-11-30: read other solutions and code by yourself
# [x] second time 20-11-30: select the best solution and use cpp to implement it
# [] third time 20-11-30: after 24 hours
# [] forth time 20-11-30: after a week
# [] fifth time 20-11-30: before interview
# @lc code=start
class Solution:
    def reversePairs(self, nums):
        return self.mergesort(nums,0,len(nums))

    def mergesort(self, nums, start, end):
        if start >= end - 1:
            return 0
        mid =  int((start + end)/ 2)
        cnt = self.mergesort(nums, start, mid) + self.mergesort(nums, mid, end)
        cnt += self.merge(nums, start, end, mid)
        return cnt

    def merge(self, nums ,start, end, mid):
        cnt = 0
        temp = []
        l, r = start, mid
        while l < mid and r < end:
            if nums[l]> 2 * nums[r]:
                cnt += mid - l
                r += 1
            else:
                l += 1

        l, r = start, mid
        while l < mid and r < end:
            if nums[l] <  nums[r]:
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[r])
                r += 1
        if l < mid:
            temp.extend(nums[l:mid])
        if r < end:
            temp.extend(nums[r:end])
        nums[start:end] = temp
        return cnt
    
        
# @lc code=end

sol = Solution()
print(sol.reversePairs([2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]))
