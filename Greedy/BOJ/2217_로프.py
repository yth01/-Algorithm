'''
import sys

n = int(sys.stdin.readline().rstrip())
w = []
for i in range(n):
    w.append(int(sys.stdin.readline().rstrip()))
w.sort(reverse=True)

result = w[0]
for i in range(1, n):
    if result < min(w[:i+1]) * (i + 1):
        result = min(w[:i+1]) * (i + 1)

print(result)
'''

import sys

n = int(sys.stdin.readline().rstrip())
w = []
for i in range(n):
    w.append(int(sys.stdin.readline().rstrip()))
w.sort(reverse=True)

result = w[0]
for i in range(1, n):
    if result < w[i] * (i + 1):
        result = w[i] * (i + 1)

print(result)


