string1, string2 = input().split(',')
len_1, l2 = len(string1), len(string2)
dp = [[0 for _ in range(l2+1)] for _ in range(len_1+1)]


for i in range(l2+1):
    dp[0][i] = i

for j in range(len_1+1):
    dp[j][0] = j

for i in range(1, len_1+1):
    for j in range(1, l2+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
print(dp[-1][-1])