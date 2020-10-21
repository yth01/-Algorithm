n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
data.append(0)

result = 0
for i in range(len(data)-1):
    result += i

count = 1
for i in range(1, len(data)-1):
    left = data[i-1]
    if left == data[i]:
        count += 1

    if count != 1 and data[i] != data[i+1]:
        for i in range(count):
            result -= i
        count = 1

print(result)

'''
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)
'''