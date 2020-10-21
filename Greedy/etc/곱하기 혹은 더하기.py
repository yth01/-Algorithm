'''
data = list(map(int, input()))

result = 0
for i in data:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)
'''

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)