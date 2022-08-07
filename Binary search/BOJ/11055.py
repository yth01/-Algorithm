n = int(input())
data = list(map(int, input().split()))

dp = [1] * n
dp[0] = data[0]
for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + data[i])
        else:
            dp[i] = max(dp[i], data[i])

print(max(dp))
