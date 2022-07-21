INF = int(1e9)

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        min_value = INF
        for k in range(3):
            if j == k:
                continue
            min_value = min(min_value, data[i-1][k])
        data[i][j] += min_value

print(min(data[n-1]))
