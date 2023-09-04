
# If you need to import additional packages or classes, please import here.
from collections import defaultdict
def map_func(x):
    if x == 0:
        return 1
    elif x == 1:
        return 3
    else:
        return 4

def func():
    num_intervals = int(input())
    intervals = []
    max_time, min_time = 0, 1000000
    for i in range(num_intervals):
        start, end = list(map(int, input().split(' ')))
        if end > max_time:
            max_time = end
        if start < min_time:
            min_time = start
        intervals.append((start, end))
    times = defaultdict(int)
    for interval in intervals:
        times[interval[0]] += 1
        times[interval[1]+1] -= 1
    times = sorted(times.items())
    result, count = 0, 0
    for i in range(len(times)-1):
        k_1, v_1 = times[i]
        k_2, v_2 = times[i+1]
        count += v_1
        if count == 0:
            result += (k_2-k_1)*1
        elif count == 1:
            result += (k_2-k_1)*3
        else:
            result += (k_2-k_1)*4
    return result

if __name__ == "__main__":
    print(func())