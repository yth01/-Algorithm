from collections import deque

n = int(input())
data = deque()
for _ in range(n):
    data.append(list(map(int, input().split())))

result = []
for i in range(n):
    height, weight = data[i]
    cnt = 1
    for h, w in data:
        if height < h and weight < w:
            cnt += 1
    result.append(cnt)

for i in result:
    print(i, end=" ")
