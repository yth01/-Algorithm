n, k = map(int, input().split())

things = [[]]
bag = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    things.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]

        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-w] + v)

print(bag[n][k])
