# input_str = list(input())
# k = int(input())
# operate_mask = [0 for _ in range(len(input_str))]
# for i in range(len(input_str)):
#     if input_str[i] == '0':
#         input_str[i] = '1'
#         k -= 1
#         operate_mask[i] = 1
#     if k == 0:
#         break

# if k > 0:
#     for i in range(len(input_str)-1, -1, -1):
#         if input_str[i] == '1' and operate_mask[i] == 0:
#             input_str[i] = '0'
#             k -= 1
#         if k == 0:
#             break
# print(''.join(input_str))


# import math 
# arr_len = int(input())
# arr = list(map(int, input().split()))
# product = 1
# for num in arr:
#     product *= num
# result = 0
# for i in range(1, int(math.sqrt(product))+1):
#     if product % i == 0:
#         result += 2 
# if int(math.sqrt(product)) ** 2 == product:
#     result -= 1
# print(result)


# arr_len = int(input())
# arr = list(map(int, input().split()))
# factors = [2] * arr_len
# for i in range(arr_len):
#     for j in range(2, int(arr[i]**0.5)+1):
#         if arr[i] % j == 0:
#             if j != arr[i] // j:
#                 factors[i] += 2
#             else:
#                 factors[i] += 1
#     if arr[i] ** 0.5 == int(arr[i] ** 0.5):
#         factors[i] -= 1
# factorcount =1 
# for i in range(arr_len):
#     factorcount *= factors[i]
# print(factorcount)


# n,m,k = list(map(int, input().split()))

# arr_1 = sorted(list(map(int, input().split())))
# arr_2 = sorted(list(map(int, input().split())))
# arr_3 = sorted(list(map(int, input().split())))
# l, r = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     if arr_1[i] > r:
#         continue
#     for j in range(m):
#         if arr_1[i] * arr_2[j] > r:
#             continue
#         for q in range(k):
#             if arr_1[i] * arr_2[j] * arr_3[q] > r:
#                 continue
#             if arr_1[i] * arr_2[j] * arr_3[q] < r and arr_1[i] * arr_2[j] * arr_3[q] > l:
#                 ans += 1
# print(ans)



# arr_len = int(input())
# arr = list(map(int, input().split()))
# factors = [2] * arr_len
# for i in range(arr_len):
#     for j in range(2, int(arr[i]**0.5)+1):
#         if arr[i] % j == 0:
#             if j != arr[i] // j:
#                 factors[i] += 2
#             else:
#                 factors[i] += 1
#     if arr[i] ** 0.5 == int(arr[i] ** 0.5):
#         factors[i] -= 1
# factorcount =1 
# for i in range(arr_len):
#     factorcount *= factors[i]
# print(factorcount % (10**9 + 7))

def trial_division(n):
    """试除法质因数分解"""
    if n < 2:
        return {}
    factors = {}
    # 尝试 2 作为质因数
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    # 尝试大于 2 的奇数
    i = 3
    while i <= n**0.5:
        if n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        else:
            i += 2
    # 如果 n > 1，则 n 是最后一个质因数
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


from collections import defaultdict
arr_len = int(input())
arr = list(map(int, input().split()))

d = defaultdict(int)
for num in arr:
    d_ = trial_division(num)
    for k, v in d_.items():
        d[k] += v 

values = list(d.values())
ans = 1 
for v in values:
    ans *= (v+1)
print(ans)