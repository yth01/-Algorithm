T = int(input())
for _ in range(T):
    n = int(input())
    d = [0] * 11
    d[0] = 1
    d[1] = 1
    d[2] = 2
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    print(d[n])
