n = int(input())
count = 0

while n > 0:
    if n % 5 == 0:
        count += 1
        n -= 5
    else:
        count += 1
        n -= 3
if n < 0:
    count = -1

print(count)