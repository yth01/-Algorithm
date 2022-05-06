k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))

start = 1
end = max(data)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in data:
        cnt += i // mid
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)
