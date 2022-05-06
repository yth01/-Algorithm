n = int(input())

num = 1
cnt = 1
while True:
    if n <= num:
        print(cnt)
        break
    num += 6 * cnt
    cnt += 1
