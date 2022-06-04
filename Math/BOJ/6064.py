import sys

def input():
    return sys.stdin.readline()[:-1]

def Calculate(m, n, x, y):
    result = x
    while result <= m * n:
        if (result - y) % n == 0:
            return result
        result += m
    return -1

T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    print(Calculate(m, n, x, y))
