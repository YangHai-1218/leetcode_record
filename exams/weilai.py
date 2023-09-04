
# dic = dict.fromkeys(['k1', 'k2', 'k3'], [])
# dic['k1'].append(1)
# dic['k2'].append(2)
# dic['k1'] = 1
# print(dic)
import sys
sys.setrecursionlimit(100000)
def f(x, n):
    if x <= 1:
        return x 
    return ((n-3) * f(x-1, n) + (n-2) * f(x-2, n)) % n

print(f(2019, 10))
# print(f(1729, 4995))
# print(f(2021, 1023)) 
# print(f(1334, 2047))


