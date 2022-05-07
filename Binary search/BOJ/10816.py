from bisect import bisect_right, bisect_left

def count_by_range(array, right, left):
    right_index = bisect_right(array, right)
    left_index = bisect_left(array, left)
    return right_index - left_index

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
data = list(map(int, input().split()))

for i in data:
    result = count_by_range(array, i, i)
    print(result if result != 0 else '0', end=' ')
