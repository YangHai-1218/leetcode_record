#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
# two stack version very slow
# but it's easy to understand
# class Solution:
#     def trap(self, height):
#         stack_1 = []
#         stack_2 = []
#         n = len(height)

#         back_max, forward_max = [-1] * n, [-1] * n
#         for i in range(n-1,-1,-1):
#             while stack_1 and height[i] >= height[stack_1[-1]]:
#                 stack_1.pop()
#             back_max[i] = stack_1[-1] if stack_1 else -1
#             stack_1.append(i)
#         for i in range(n):
#             while stack_2 and height[i] >= height[stack_2[-1]]:
#                 stack_2.pop()
#             forward_max[i] = stack_2[-1] if stack_2 else -1
#             stack_2.append(i)
#         print(f'back_max:{back_max}')
#         print(f'forward_max:{forward_max}')
#         ans = 0
#         for _ in range(20):
#             for i in range(n):
#                 if back_max[i] != -1 and forward_max[i] != -1:
#                     temp = min(height[back_max[i]], height[forward_max[i]]) - height[i]
#                     ans += temp
#                     height[i] += temp
#         print(f'after fill height:{height}')
#         return ans


# one stack version
class Solution:
    def trap(self, height):
        stack = []
        n = len(height)
        ans = 0
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                idx = stack.pop()
                while stack and height[stack[-1]] == height[idx]:
                    stack.pop()
                
                # i - stack[-1] - 1 为宽度
                # min(height[i], height[stack[-1]]) - height[idx]) 为 填充雨水的高度
                ans += (min(height[i], height[stack[-1]]) - height[idx]) * (i-stack[-1]-1) if stack else 0
                
            stack.append(i)
        return ans
# @lc code=end

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
