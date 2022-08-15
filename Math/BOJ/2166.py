n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

nx, ny = 0, 0
for i in range(n):
    nx += x[i] * y[i+1]
    ny += y[i] * x[i+1]

print(round(abs((nx-ny)/2), 1))
