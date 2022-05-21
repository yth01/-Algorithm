T = int(input())
for _ in range(T):
    n = int(input())
    d = [0] * 41
    d[0] = 0
    d[1] = 1

    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    if n == 0:
        print(1, 0)
    else:
        print(d[n-1], d[n])
