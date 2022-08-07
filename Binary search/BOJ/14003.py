from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]
length = [0] * n
length[0] = 1

for i in range(1, n):
    if A[i] > dp[-1]:
        dp.append(A[i])
        length[i] = len(dp)
    else:
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]
        length[i] = idx + 1

max_cnt = max(length)
max_idx = length.index(max_cnt)
result = []

while max_idx >= 0:
    if length[max_idx] == max_cnt:
        result.append(A[max_idx])
        max_cnt -= 1
    max_idx -= 1

print(len(result))
print(*result[::-1])
