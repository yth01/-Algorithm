import sys

n = int(input())
data = list(map(int, input().split()))
data.sort()

min_value = sys.maxsize
result = []

for fix in range(n):
    left = 0
    right = n-1
    while left < right:
        if left == fix:
            left += 1
        elif right == fix:
            right -= 1
        if left == right:
            break
        
        if abs(data[left] + data[right] + data[fix]) < min_value:
            min_value = abs(data[left] + data[right] + data[fix])
            result = [data[left], data[right], data[fix]]

        if data[left] + data[right] + data[fix] < 0:
            left += 1
        else:
            right -= 1

print(*sorted(result))
