n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(input())

result = []
for a in range(n - 7):
    for b in range(m - 7):
        w_cnt = 0
        b_cnt = 0 
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i + j) % 2 == 0:
                    if data[i][j] != 'W':
                        w_cnt += 1
                    if data[i][j] != 'B':
                        b_cnt += 1
                else:
                    if data[i][j] != 'B':
                        w_cnt += 1
                    if data[i][j] != 'W':
                        b_cnt += 1
        result.append(min(w_cnt, b_cnt))

print(min(result))    
