n, m = map(int, input().split())

dict = {}
for _ in range(n):
    a, b = input().split()
    dict[a] = b

for _ in range(m):
    print(dict[input()])
