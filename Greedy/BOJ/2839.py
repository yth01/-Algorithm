n = int(input())

cnt = 0
while n > 0:
    if n % 5 == 0:
        n -= 5
        cnt += 1
    else: 
        n -= 3
        cnt += 1
if n < 0:
    cnt = -1

print(cnt)
