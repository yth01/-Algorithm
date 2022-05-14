num = 1
for _ in range(3):
    num *= int(input())

data = list(map(int, list(str(num))))
result = [0 for _ in range(10)]
for i in data:
    result[i] += 1

for i in result:
    print(i)
