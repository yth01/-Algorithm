n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

count = 0
for i in a:
    if k // i > 0:
        count += k // i
        k %= i

print(count)
