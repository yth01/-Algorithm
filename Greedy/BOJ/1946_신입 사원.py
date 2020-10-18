import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    data = []
    for _ in range(n):
        data.append(list(map(int, sys.stdin.readline().split())))
    data.sort(key=lambda x:x[0])

    count = 1
    min = data[0][1]
    for i in range(1, n):
        if data[i][1] < min:
            min = data[i][1]
            count += 1

    print(count)







