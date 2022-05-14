import math

a, b, v = map(int, input().split())

v -= a
day = 1
day += v / (a-b)

print(math.ceil(day))
