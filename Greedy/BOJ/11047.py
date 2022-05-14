n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0
for coin in coins:
    if k // coin:
        cnt += k // coin
        k = k % coin

print(cnt)
