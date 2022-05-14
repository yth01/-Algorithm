a = [0 for i in range(23)]
n = int(input())
b = list(map(int, input().split()))
for i in b:
    a[i-1] += 1
for i in range (23):
    print(a[i], end=' ')
