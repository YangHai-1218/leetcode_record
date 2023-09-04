# seq_len = int(input())
# nums = list(map(int, input().split()))
# for i in range(1, seq_len):
#     nums[i] += max(nums[i - 1], 0)
# print(max(nums))


# import collections
# from heapq import heappop, heappush
# from typing import List
# class DualHeap:
#     def __init__(self, k):
#         self.small = []
#         self.large = []
#         self.delayed = collections.Counter()

#         self.k = k 
#         self.smallsize = 0
#         self.largesize = 0
    
#     def prune(self,heap):
#         while heap:
#             num = heap[0]
#             if heap is self.small:
#                 num = -num
#             if num in self.delayed:
#                 self.delayed[num] -= 1
#                 if self.delayed[num] == 0:
#                     self.delayed.pop(num)
#                 heappop(heap)
#             else:
#                 break
        

#     def makebalance(self):
#         if self.smallsize > self.largesize + 1:
#             heappush(self.large, -self.small[0])
#             heappop(self.small)
#             self.smallsize -= 1
#             self.largesize += 1
#             self.prune(self.small)
#         elif self.smallsize < self.largesize:
#             heappush(self.small, -self.large[0])
#             heappop(self.large)
#             self.smallsize += 1
#             self.largesize -= 1
#             self.prune(self.large)
    
#     def insert(self, num):
#         if not self.small or num <= -self.small[0]:
#             heappush(self.small, -num)
#             self.smallsize += 1
#         else:
#             heappush(self.large, num)
#             self.largesize += 1
#         self.makebalance()
    
#     def erase(self, num):
#         self.delayed[num] += 1
#         if num <= -self.small[0]:
#             self.smallsize -= 1
#             if num == -self.small[0]:
#                 self.prune(self.small)
#         else:
#             self.largesize -= 1
#             if num == self.large[0]:
#                 self.prune(self.large)
#         self.makebalance()

#     def getmedian(self):
#         if self.k % 2 == 1:
#             return -self.small[0]
#         else:
#             return (-self.small[0] + self.large[0])/2

# def format_number(num):
#     if num % 1 == 0:
#         return int(num)
#     else:
#         return round(num, len(str(num).split('.')[-1]))

# class Solution:
#     def slidewindow(self , nums: List[int], k: int) -> List[float]:
#         dualheap = DualHeap(k)
#         for num in nums[:k]:
#             dualheap.insert(num)

#         ans = [dualheap.getmedian()]
#         for i in range(k, len(nums)):
#             dualheap.insert(nums[i])
#             dualheap.erase(nums[i-k])
#             ans.append(dualheap.getmedian())
#         ans = [format_number(a) for a in ans]
#         return ans



# input_seq = input()[1:]
# nums, k = input_seq.split('],')
# nums = list(map(int, nums.split(',')))
# k = int(k)
# Solution().slidewindow(nums, k)

from typing import List
class Solution:
    def rotApple(self , grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        queue = []

        count = 0
        for j in range(M):
            for i in range(N):
                if grid[j][i] == 1:
                    count += 1
                elif grid[j][i] == 2:
                    queue.append((j, i))
        

        rot_round = 0
        while count > 0 and len(queue) > 0:
            rot_round += 1
            n = len(queue)
            for _ in range(n):
                j, i = queue.pop(0)
                if j - 1 >=0 and grid[j-1][i] == 1:
                    grid[j-1][i] = 2
                    count -= 1
                    queue.append((j-1, i))
                if j + 1 < M and grid[j+1][i] == 1:
                    grid[j+1][i] = 2
                    count -= 1
                    queue.append((j+1, i))
                
                if i - 1 >= 0 and grid[j][i-1] == 1:
                    grid[j][i-1] = 2
                    count -= 1
                    queue.append((j, i-1))
                
                if i + 1 < N and grid[j][i+1] == 1:
                    grid[j][i+1] = 2
                    count -= 1
                    queue.append((j, i+1))
        if count > 0:
            return -1
        else:
            return rot_round
    

import collections
class Solution:

    def neighbors_find(self, j, i, M, N):
        for nr, nc in ((j - 1, i), (j, i - 1), (j + 1, i), (j, i + 1)):
            if 0 <= nr < M and 0 <= nc < N:
                yield nr, nc

    def rotApple(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        queue = collections.deque()
        for j, row in enumerate(grid):
            for i, val in enumerate(row):
                if val == 2:
                    queue.append((j, i, 0))

        d = 0
        while queue:
            j, i, d = queue.popleft()
            for nr, nc in self.neighbors_find(j, i, M, N):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d
    

