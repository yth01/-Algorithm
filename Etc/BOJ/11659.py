import sys

def input():
    return sys.stdin.readline()[:-1]

n, m = map(int, input().split())
data = list(map(int, input().split()))

num = 0
prefix_sum = [0]
for i in data:
    num += i
    prefix_sum.append(num)

for _ in range(m):
    left, right = map(int, input().split())
    print(prefix_sum[right] - prefix_sum[left - 1])
