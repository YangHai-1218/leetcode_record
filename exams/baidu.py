# num_cases = int(input())
# for i in range(num_cases):
#     case_len, case = input().split()
#     case_len = int(case_len)
#     case += '0'
#     i = 0
#     counts = 0
#     while i < case_len:
#         c = case[i]
#         if c == '1':
#             while i < case_len and c == '1':
#                 i += 1
#                 c = case[i]
#             counts += 1
#         else:
#             i += 1
#     print(counts)


# case_len, case = input().split()
# case_len = 8
# case = '00011101'
# case += '0'
# case_len = int(case_len)
# i = 0
# counts = 0
# while i < case_len:
#     c = case[i]
#     if c == '1':
#         while i < case_len and c == '1':
#             i += 1
#             c = case[i]
#         counts += 1
#     else:
#         i += 1


# len_input = int(input())
# nums = list(map(int, input().split()))
# curYes, curNo = 0, 0
# for i in range(len(nums)):
#     temp = curNo
#     curNo = max(curYes, curNo)
#     curYes = temp + nums[i]
# print(max(curYes, curNo))


len_input = int(input())
nums = list(map(int, input().split()))
sums = [0 for _ in range(1000001)]
take, skip = 0, 0
for n in nums:
    sums[n] += n 

for i in range(1000001):
    takei = skip + sums[i]
    skipi = max(skip, take)
    take = takei
    skip = skipi 
print(max(skip, take))


