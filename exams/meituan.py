# problem 1
# numbers = "11551111"
# numbers = list(map(int, list(numbers)))
# n = len(numbers)
# count = 0
# i = 1
# while i < n:
#     if i < n-1 and numbers[i] == numbers[i-1] and numbers[i] == numbers[i+1]:
#         count += 1
#         i += 2
#     elif numbers[i] == numbers[i-1]:
#         count += 1
#         i += 1
#     else:
#         i += 1
# print(count)


# problem 2 流星
# intervals = int(input())
# start = input()
# end = input()
# start = list(map(int, start.split()))
# end = list(map(int, end.split()))
# min_time = min(start)
# max_time = max(end)

# time_mask = [0 for _ in range(min_time, max_time+1)]
# for i in range(intervals):
#     time_mask_temp = time_mask[start[i]-min_time:end[i]+1-min_time]
#     time_mask_temp = [t+1 for t in time_mask_temp]
#     time_mask[start[i]-min_time:end[i]+1-min_time] = time_mask_temp
# x = max(time_mask)
# y = 0
# for t in time_mask:
#     if t == x:
#         y += 1
# print(f"{x} {y}")
from collections import defaultdict, OrderedDict

start = [2,1,5]
end = [6,3,7]
mp = defaultdict(int)
time_interval = [(s,e) for s, e in zip(start, end)]
time_interval.sort(key=lambda x:x[0])
for s, e in time_interval:
    mp[s] += 1
    mp[e+1] -= 1

mp = OrderedDict(sorted(mp.items()))
sum = 0
for t in mp:
    sum += mp[t]
    mp[t] = sum

max_stars = -1 
for s in mp.values():
    max_stars = max(max_stars, s)
print(max_stars)

max_star_time = 0
v_list = [(k, v) for k, v in mp.items()]
v_list.sort(key=lambda x:x[0])
for i, v in enumerate(v_list):
    if v[1] != max_stars:
        continue
    elif i == len(v_list) -1:
        max_star_time += 1 
    else:
        max_star_time += v_list[i+1][0] - v_list[i][0]
print(max_star_time)

        


# problem 4(坦克大战)
# def shoot_success(position_a, position_b):
#     direction = position_a[-1]
#     if direction == 'U':
#         if position_a[-2] == position_b[-2] and position_b[0] < position_a[0]:
#             return True
#     elif direction == 'D':
#         if position_a[-2] == position_b[-2] and position_b[0] > position_a[0]:
#             return True
#     elif direction == 'R':
#         if position_a[0] == position_b[0] and position_b[1] < position_a[1]:
#             return True
#     else:
#         if position_a[0] == position_b[0] and position_b[1] > position_a[1]:
#             return True
#     return False

# # (y,x, direction)
# d = [0, 0, 0]
# w = [15, 15, 0]
# # 0 未被占领 1 被d占领 -1 被w占领
# positions = [[0 for _ in range(16)] for _ in range(16)]
# d_commands = input().split()
# w_commands = input().split()
# len_commands = len(d_commands)
# for i in range(len_commands):
#     # d_command 
#     if d_commands[i] == 'U':
#         if positions[d[0]-1, d[1]] != '-1':
#             d[0] -= 1
#             positions[d[0], d[1]] = 1
#         else:
#             d[-1] = 'U'
#     elif d_commands[i] == 'D':
#         if positions[d[0]+1, d[1]] != '-1':
#             d[0] += 1
#             positions[d[0], d[1]] = 1
#         else:
#             d[-1] = 'D'
#     elif d_commands[i] == 'R':
#         if positions[d[0], d[1]+1] != '-1':
#             d[1] += 1
#             positions[d[0], d[1]] = 1
#         else:
#             d[-1] = 'R'
#     elif d_commands[i] == 'L':
#         if positions[d[0], d[1]-1] != '-1':
#             d[1] -= 1
#             positions[d[0], d[1]] = 1
#         else:
#             d[-1] = 'L'
#     elif d_commands[i] == 'F':
#         if shoot_success(d,w):
#             print(i+1, "D")
#             break
#     else:
#         continue

#     # w_command 
#     if w_commands[i] == 'U':
#         if positions[w[0]-1, w[1]] != '1':
#             w[0] -= 1
#             positions[w[0], w[1]] = 1
#         else:
#             w[-1] = 'U'
#     elif w_commands[i] == 'D':
#         if positions[w[0]+1, w[1]] != '1':
#             w[0] += 1
#             positions[w[0], w[1]] = 1
#         else:
#             w[-1] = 'D'
#     elif w_commands[i] == 'R':
#         if positions[w[0], w[1]+1] != '1':
#             w[1] += 1
#             positions[w[0], w[1]] = 1
#         else:
#             w[-1] = 'R'
#     elif w_commands[i] == 'L':
#         if positions[w[0], w[1]-1] != '-1':
#             w[1] -= 1
#             positions[w[0], w[1]] = 1
#         else:
#             w[-1] = 'L'
#     elif w_commands[i] == 'F':
#         if shoot_success(w,d):
#             print(i+1, "W")
#             break
#     else:
#         continue

