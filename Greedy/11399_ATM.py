n = int(input())
p = sorted(list(map(int, input().split())))

result = p[0]

for i in range(1, n):
    p[i] += p[i-1]
    result += p[i]

print(result)
