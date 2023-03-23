# num_treenodes = int(input())
# input_treenodes = input()
# dummpy_treenode = 'F'
# input_treenodes = dummpy_treenode + input_treenodes


# result = 0
# for i in range(1, len(input_treenodes)):
#     if 2*i > len(input_treenodes)-1:
#         continue
#     if input_treenodes[2*i] != input_treenodes[2*i+1]:
#         result += 1
    
# print(2**result)

n, x  = list(map(int, input().split()))
input_cost = list(map(int, input().split(' ')))
input_str = input()
dp = [0 for _ in range(n)]
if n == 0:
    print(0)
elif n == 1:
    print(input_cost[0])
else:
    dp[0] = input_cost[0]
    if input_str[0] != input_str[1]:
        dp[1] = min(x, input_cost[0]+input_cost[1])
    else:
        dp[1] = input_cost[0]+input_cost[1]
    for i in range(2, n):
        if dp[i] != dp[i-1]:
            dp[i] = min(dp[i-2]+x, dp[i-1]+input_cost[i])
        else:
            dp[i] = dp[i-1] + input_cost[i]
    print(dp[-1])
        
