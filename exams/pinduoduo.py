# num_peoples = int(input())
# choices = []
# for i in range(num_peoples):
#     choices.append(input())
# limits, prices = [], []
# for i in range(3):
#     limit, price = list(map(int, input().split()))
#     limits.append(limit)
#     prices.append(price)

# assigned_mask = [-1 for _ in range(num_peoples)]

# # 1 step
# for i, choice in enumerate(choices):
#     if len(choice) == 1:
#         limits[ord(choice)-ord('A')] -= 1
#         assigned_mask[i] = ord(choice)-ord('A')

# if any(map(lambda x:x<0, limits)):
#     print("No")
#     # TODO 

# # choose the current assigned activity
# min_price = min(prices)
# min_index = [i for i,p in enumerate(prices) if p==min_price][0]
# max_price = max(prices)
# max_index = [i for i,p in enumerate(prices) if p==max_price][0]
# mid_index = [i for i in range(3) if i not in [min_index, max_index]][0]
# sorted_index = [min_index, mid_index, max_index]

# current_index = 0
# if limits[sorted_index[current_index]] < 0:
#     current_index += 1
#     if limits[sorted_index[current_index]] < 0:
#         current_index += 1


# while not (all(map(lambda x:x!=-1, assigned_mask)) or any(map(lambda x:x<0, limits))):
#     for i, choice in enumerate(choices):
#         if len(choice) > 1 and assigned_mask[i]== -1:
#             if "ABC"[sorted_index[current_index]] in choice:
#                 limits[sorted_index[current_index]] -= 1
#                 assigned_mask[i] = ord( "ABC"[sorted_index[current_index]]) - ord('A')
#             if limits[sorted_index[current_index]] <= 0:
#                 current_index += 1
#                 if current_index >= 3:
#                     break
                    
# if all(map(lambda x:x!=-1, assigned_mask)):
#     print("YES")
#     print(sum([prices[m] for m in assigned_mask]))
# else:
#     print("No")
#     # TODO


# 输入两行：第一行为一个整数N，表示餐厅营业总天数（0<N<200,000），第二行共N个整数
# 输出：第一行长度为N，第i个值表示前i个数的平均值，第二行长度为N，第i个值表示前i个数的中位数
import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]


nm_numbers = int(input())
numbers = list(map(int, input().split()))
numbers = numbers[:nm_numbers+1]

averge_list = []
for n in numbers:
    if len(averge_list) == 0:
        averge_list.append(n)
    else:
        averge_list.append((len(averge_list)*averge_list[-1]+n)/(len(averge_list)+1))
print(''.join([str(int(a+0.5))+' ' for a in averge_list])[:-1])

median_finder = MedianFinder()
median_list = []
for n in numbers:
    median_finder.addNum(n)
    median_list.append(median_finder.findMedian())
print(''.join([str(int(m+0.5))+' ' for m in median_list])[:-1])