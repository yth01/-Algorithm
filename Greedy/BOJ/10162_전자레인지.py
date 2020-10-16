t = int(input())

result = [0, 0, 0]
count = 0
for i in [300, 60, 10]:
    if t // i > 0:
        result[count] += t // i
        t %= i
    count += 1

if t != 0:
    print(-1)
else:
    for i in result:
        print(i, end=' ')
