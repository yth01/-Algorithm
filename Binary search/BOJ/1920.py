def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
data = list(map(int, input().split()))

for i in data:
    result = binary_search(array, i, 0, len(array)-1)
    if result != None:
        print(1)
    else:
        print(0)
