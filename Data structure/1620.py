n, m = map(int, input().split())

dict = {}
for i in range(1, n+1):
    dist = input()
    dict[i] = dist
    dict[dist] = i

for _ in range(m):
    dist = input()
    if dist.isdigit():
        print(dict[int(dist)])
    else:
        print(dict[dist])
