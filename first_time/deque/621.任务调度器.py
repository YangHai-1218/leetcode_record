#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start

# simulate version
# from collections import defaultdict
# class Solution:
#     def leastInterval(self, tasks, n):
#         if n == 0:
#             return len(tasks)
#         order_list = []
#         order_list_2 = []
#         dic = defaultdict(int)
#         total_task_num = 0
#         for task in tasks:
#             dic[task] += 1
#             total_task_num += 1
#         num = 0
#         ans = 0
#         while num < total_task_num:
#             if order_list:
#                 if ans - order_list_2[0] > n:
#                     order_list.pop(0)
#                     order_list_2.pop(0)
#             # if len(order_list) < n:
#             max_left = float('-inf')
#             for task in dic:
#                 if task not in order_list and dic[task] > 0:
#                     if dic[task] > max_left:
#                         max_left = dic[task]
#                         max_left_task = task
#             if max_left != float('-inf'):
#                 order_list.append(max_left_task)
#                 order_list_2.append(ans)
#                 num += 1
#                 dic[max_left_task] -= 1
#             ans += 1
#         return ans

# simplified version
from collections import defaultdict
class Solution:
    def leastInterval(self, arr, n):
        dic = defaultdict(int)
        for task in arr:
            dic[task] += 1
        max_time_task = max([dic[task] for task in dic])
        ans = (max_time_task - 1) * (n+1)
        for task in dic:
            if dic[task] == max_time_task:
                ans += 1
        return ans if ans >= len(arr) else len(arr)


# @lc code=end

tasks = ["A","A","A","B","B","B","C","C","C","D","D","D"]
n = 2
sol = Solution()
print(sol.leastInterval(tasks, n))