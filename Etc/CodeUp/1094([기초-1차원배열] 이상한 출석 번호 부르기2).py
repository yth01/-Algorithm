n = int(input())
a = list(reversed(list((map(int, input().split())))))
for i in range (n):
    print(a[i], end=' ')
