import sys
input = sys.stdin.readline
    
target = int(input())
m = int(input())
broken = list(map(int, input().split()))

result =  abs(target - 100)
for num in range(1000001):
    nums = list(str(num))
    for i in range(len(nums)):
        if int(nums[i]) in broken:
            break
        elif i == len(nums)-1:
            result = min(result, len(nums)+abs(num-target))

print(result)
