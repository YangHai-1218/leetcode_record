#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# [x] first time 20-11-09: code by yourself and read other solutions
# [] second time 20-11-09: select the best solution and implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# tag: array two-pointers
# @lc code=start
class Solution:
    def threeSum(self, nums):
        if nums == [] or len(nums)<3:
            return []
        nums = sorted(nums)
        len_nums = len(nums)
        res = []
        num_i = nums[0]-1
        i = 0
        for i in range(len_nums):
            if num_i >0:
                return res  

            if nums[i] == num_i:
                continue
            num_i = nums[i]

            j, k = i+1,len_nums-1
            
            while j<k:
                num_j, num_k = nums[j],nums[k]
                if num_i + nums[j] + nums[k] < 0:
                    j += 1
                    while nums[j] == num_j and j<k:
                        j+= 1
                elif num_i + nums[j] + nums[k] > 0:
                    k -= 1
                    while nums[k] == num_k and j<k:
                        k -= 1
                else:
                    res.append((num_i, nums[j], nums[k]))
                    j,k = j+1, k-1
                    while nums[j] == num_j and j<k:
                        j += 1
                    while nums[k] == num_k and j<k:
                        k -= 1
        return res


# @lc code=end


sol = Solution()
print(sol.threeSum([0,0,0]))
