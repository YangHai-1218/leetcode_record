#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# [x] first time 20-11-09: read other solutions and code by yourself
# [] second time 20-11-09: select the best solution and use cpp to implement it
# [] third time 20-11-09: after 24 hours
# [] forth time 20-11-09: after a week
# [] fifth time 20-11-09: before interview
# @lc code=start
# class Solution:
#     def plusOne(self, digits):
#         n = len(digits)
#         if digits[n-1] != 9:
#             digits[n-1] += 1
#             return digits
#         else:
#             for i in range(n-1,-1,-1):
#                 if i!=0:
#                     if digits[i] == 9:
#                         digits[i] = 0
#                     else:
#                         digits[i] += 1
#                         return digits
#                 else:

#                     if digits[i] != 9:
#                         digits[i] += 1
#                     else:
#                         digits[i] = 0
#                         digits.insert(0,1)
#                     return digits
#         return digits

# version II
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
                    return digits
            else:
                digits[i] += 1
                return digits        


# @lc code=end

sol = Solution()
print(sol.plusOne([2,4,9,3,9]))

