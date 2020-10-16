k = 1000 - int(input())
count = 0
for i in [500, 100, 50, 10, 5, 1]:
    if k // i > 0:
        count += k // i
        k %= i
print(count)
