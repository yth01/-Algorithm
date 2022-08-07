n = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_cnt = max(dp)
max_idx = dp.index(max_cnt)
result = []
while max_idx >= 0:
    if dp[max_idx] == max_cnt:
        result.append(A[max_idx])
        max_cnt -= 1
    max_idx -= 1

result.reverse()
print(len(result))
print(*result)
