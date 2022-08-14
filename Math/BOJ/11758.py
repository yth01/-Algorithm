data = []
for _ in range(3):
    data.append(list(map(int, input().split())))

def ccw(a, b, c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(b[0]*a[1]+a[0]*c[1]+c[0]*b[1])

result = ccw(data[0], data[1], data[2])
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
