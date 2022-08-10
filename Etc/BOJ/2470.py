import sys

n = int(input())
data = list(map(int, input().split()))
data.sort()

left = 0
right = n-1
min_value = sys.maxsize
result = []

while left < right:
    if abs(data[left] + data[right]) < min_value:
        min_value = abs(data[left] + data[right])
        result = [data[left], data[right]]

    if data[left] + data[right] < 0:
        left += 1
    else:
        right -= 1

print(*result)
