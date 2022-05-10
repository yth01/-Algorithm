import math

n = int(input())
array = list(map(int, input().split()))

num = 1001
data = [True for _ in range(num+1)]

for i in range(2, int(math.sqrt(num))+1):
    if(data[i] == True):
        j = 2
        while i*j <= num:
            data[i*j] = False
            j += 1

data[1] = False
result = 0
for i in array:
    if data[i]:
        result += 1
print(result)
