# def find_most_frequent_char(s):
#     # 定义一个空字典用于存储每个字符出现的次数
#     count_dict = {}
    
#     # 遍历字符串中的每个字符，更新字典中每个字符的计数器
#     for c in s:
#         if c in count_dict:
#             count_dict[c] += 1
#         else:
#             count_dict[c] = 1
    
#     # 遍历字典中的所有键值对，找到计数器最大的键
#     max_count = 0
#     max_chars = []
#     for c, count in count_dict.items():
#         if count > max_count:
#             max_count = count
#             max_chars = [c]
#         elif count == max_count:
#             max_chars.append(c)
    
#     # 返回出现次数最多的字符
#     return max_chars

# def reverse_case(c):
#     # 将字符全部转换成大写或小写
#     c_lower = c.lower()
#     c_upper = c.upper()
    
#     # 将大写字母转换成小写字母，小写字母转换成大写字母
#     if c == c_lower:
#         return c_upper
#     else:
#         return c_lower



# n, q = map(lambda x:int(x), input().split(' '))
# input_str = input()
# input_str = list(input_str)
# for j in range(q):
#     l, r = map(lambda x:int(x), input().split(' '))
#     chars = find_most_frequent_char(input_str[l-1:r])
#     for i in range(l-1, r):
#         if input_str[i] in chars:
#             input_str[i] = reverse_case(input_str[i])
#     print(''.join(input_str))


# def get_odd_even_numbers(n):
#     # 定义两个空列表，用于存储奇数和偶数
#     odds = []
#     evens = []
    
#     # 遍历从 1 到 n 的所有整数，将奇数和偶数分别放到不同的列表中
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             evens.append(i)
#         else:
#             odds.append(i)
    
#     # 返回奇数和偶数列表
#     return odds, evens


# n = int(input())
# input_01 = input()
# result = []
# odds, evens = get_odd_even_numbers(n)
# len_odds, len_evens = len(odds), len(evens)
# odd_index, even_index = 0, 0
# for i in range(n):
#     if i == 0:
#         if input_01[i] == '0':
#             result.append(evens[even_index])
#             even_index += 1
#         else:
#             result.append(odds[odd_index])
#             odd_index += 1
#     else:
#         if input_01[i] == input_01[i-1]:
#             result.append(evens[even_index])
#             even_index += 1
#         else:
#             result.append(odds[odd_index])
#             odd_index += 1
# result_str = []
# for i in range(len(result)):
#     if i != len(result)-1:
#         result_str.append(str(result[i]))
#         result_str.append(' ')
#     else:
#         result_str.append(str(result[i]))
# print(''.join(result_str))
# def expected_removal_count(a):
#     # 计算数组元素之和
#     total_sum = sum(a)
    
#     # 如果数组为空，则期望删除次数为 0
#     if total_sum == 0 or len(a) == 0:
#         return 0
    
# #     # 计算每个元素被选中的概率
# #     p = [x / total_sum for x in a]
    
# #     # 计算每个元素被选中后的期望删除次数
# #     expected_counts = [1 + expected_removal_count(a[i+1:]) for i in range(len(a))]
# #     expected_counts.reverse()
    
# #     # 计算期望删除次数的加权平均
# #     expected_count = sum([p[i] * expected_counts[i] for i in range(len(a))])
    
# #     return expected_count


# def expected_removal_count(a, mem):
#     # 判断是否已经计算过当前数组的期望删除次数
#     key = tuple(a)
#     if key in mem:
#         return mem[key]
    
#     # 计算数组元素之和
#     total_sum = sum(a)
    
#     # 如果数组为空，则期望删除次数为 0
#     if total_sum == 0 or len(a) == 0:
#         return 0
    
#     # 计算每个元素被选中的概率
#     p = [x / total_sum for x in a]
    
#     # 计算每个元素被选中后的期望删除次数
#     expected_counts = [1 + expected_removal_count(a[i+1:], mem) for i in range(len(a))]
    
#     # 计算期望删除次数的加权平均
#     expected_count = sum([p[i] * expected_counts[i] for i in range(len(a))])
    
#     # 将当前数组的期望删除次数存入字典中
#     mem[key] = expected_count
    
#     return expected_count


def expected_removal_count(a, tgt):
    # 计算数组元素之和
    total_sum = sum(a)
    
    # 如果数组为空，则期望删除次数为 0
    if total_sum == tgt:
        return 0

    
    # 计算每个元素被选中的概率
    p = [x / total_sum for x in a]
    
    # 计算每个元素被选中后的期望删除次数
    expected_counts = [1 + expected_removal_count(a[:i+1], tgt) for i in range(len(a))]
    
    # 计算期望删除次数的加权平均
    expected_count = sum([p[i] * expected_counts[i] for i in range(len(a))])
    
    return expected_count



n = int(input())
input_list = list(map(lambda x:int(x), input().split(' ')))
print(expected_removal_count(input_list, sum(input_list)))
# dp = [0 for _ in range(n)]
# total_sum = sum(input_list)
# p = [x/total_sum for x in input_list]
# dp[0] = p[0]
# for i in range(1, n):
#     cur_list = input_list[:i]
#     cur_sum = sum(cur_list)
#     cur_p = [x/cur_sum for x in cur_list]
#     cur_dp = [dp[j] * cur_p[j] for j in range(i)]
#     cur_dp.append(1+)
#     dp[i] = dp[i-1]*cur_p[]
#     dp[i] = dp[i-1] + (dp[i-1] + 1)* p[i]
# print(dp[-1])

