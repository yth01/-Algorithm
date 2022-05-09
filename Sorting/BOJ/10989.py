import sys

n = int(sys.stdin.readline().rstrip())
data = [0 for _ in range(10001)]

for _ in range(n):
    data[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            print(i)
