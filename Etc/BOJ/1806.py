INF = int(1e9)

n, s = map(int, input().split())
data = list(map(int, input().split()))

interval_sum = 0
end = 0
length = INF

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum >= s:
        length = min(length, end-start)
    interval_sum -= data[start]

print(length if length != INF else 0)
