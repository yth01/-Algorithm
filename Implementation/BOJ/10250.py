T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())

    cnt = 1
    while n > h:
        n -= h
        cnt += 1
    
    if len(str(cnt)) == 1:
        print(str(n) + '0' + str(cnt))
    else:
        print(str(n) + str(cnt))
