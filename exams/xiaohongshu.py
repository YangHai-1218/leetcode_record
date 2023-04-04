# len_input = int(input())
# input_str = input()


# def reverse(char):
#     ord_char = ord(char)-ord('a')
#     ord_char = ord_char - 3
#     if ord_char < 0:
#         ord_char = 26 + ord_char
#     return 'abcdefghijklmnopqrstuvwxyz'[ord_char]

# result = []
# for char in input_str:
#     result.append(reverse(char))
# print(''.join(result))

def youxu_array(nums, mask):
    new_nums = []
    for n, m in zip(nums, mask):
        if not m:
            new_nums.append(n)
    for i in range(len(new_nums)-1):
        if new_nums[i] > new_nums[i+1]:
            return False
    return True

input_cases = int(input())
for _ in range(input_cases):
    n, k = list(map(int, input().split(' ')))
    input_nums = list(map(int, input().split(' ')))
    mask = [False for _ in range(n)]
    result = 1
    while not youxu_array(input_nums, mask):
        for i in range(n):
            if n- result*k < input_nums[i] <= n-(result-1)*k:
                mask[i] = True 
        result += 1
    print(result - 1)

def op_1(nums, l, r, x):
    for i in range(l-1, r):
        nums[i] = nums[i] | x 

def op_2(nums, l, r, x):
    for i in range(l-1, r):
        nums[i] = nums[i] & x 

def op_3(nums, l, r, x):
    for i in range(l-1, r):
        nums[i] = x 

len_input = int(input())
input_nums = list(map(int, input().split(' ')))
op_nums = int(input())
seq_l = list(map(int, input().split(' ')))
seq_r = list(map(int, input().split(' ')))
seq_op = input()
seq_x = list(map(int, input().split(' ')))

for i in range(op_nums):
    if seq_op[i] == '|':
        op_1(input_nums, seq_l[i], seq_r[i], seq_x[i])
    elif seq_op[i] == '&':
        op_2(input_nums, seq_l[i], seq_r[i], seq_x[i])
    elif seq_op[i] == '=':
        op_3(input_nums, seq_l[i], seq_r[i], seq_x[i])
result = ''
for n in input_nums:
    result = result +f' {n}'
print(result[1:])
