n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    data[i][0] += min(data[i-1][1], data[i-1][2])
    data[i][1] += min(data[i-1][0], data[i-1][2])
    data[i][2] += min(data[i-1][0], data[i-1][1])
result = min(data[n-1][0], data[n-1][1], data[n-1][2])

print(result)