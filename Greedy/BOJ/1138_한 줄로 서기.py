n = int(input())
data = list(map(int, input().split()))
result = [0 for i in range(n)]

for i in range(1, n+1):
    height = data[i-1]
    count = 0
    for j in range(n):
        if result[j] == 0:
            if count == height:
                result[j] = i
                break
            else:
                count += 1

for i in result:
    print(i, end=' ')

