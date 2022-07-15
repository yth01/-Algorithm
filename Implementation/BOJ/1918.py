import sys


def input():
    return sys.stdin.readline()[:-1]


def top_air_cleaning(now_r, now_c, pre_dust, flag):
    if data[now_r][now_c] == -1:
        return
    
    next_r = now_r
    if not flag:
        next_c = now_c + 1            
        if next_c >= c:
            next_r -= 1
            next_c -= 1
            if next_r < 0:
                flag = True
                next_r += 1
                next_c -= 1
    else:
        next_c = now_c - 1
        if next_c < 0:
            next_r += 1
            next_c += 1
    
    now_dust = data[now_r][now_c]
    data[now_r][now_c] = pre_dust

    top_air_cleaning(next_r, next_c, now_dust, flag)


def bottom_air_cleaning(now_r, now_c, pre_dust, flag):
    if data[now_r][now_c] == -1:
        return
    
    next_r = now_r
    if not flag:
        next_c = now_c + 1
        if next_c >= c:
            next_r += 1
            next_c -= 1
            if next_r >= r:
                flag = True
                next_r -= 1
                next_c -= 1
    else:
        next_c = now_c - 1
        if next_c < 0:
            next_r -= 1
            next_c += 1
    
    now_dust = data[now_r][now_c]
    data[now_r][now_c] = pre_dust

    bottom_air_cleaning(next_r, next_c, now_dust, flag)


def spread():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    temp_data = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if data[i][j] > 0:
                temp = 0
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0 <= nr < r and 0 <= nc < c and data[nr][nc] != -1:
                        temp_data[nr][nc] += data[i][j] // 5
                        temp += data[i][j] // 5
                data[i][j] -= temp
    
    for i in range(r):
        for j in range(c):
            data[i][j] += temp_data[i][j]


r, c, t = map(int, input().split())
data = []
for _ in range(r):
    data.append(list(map(int, input().split())))

air_cleaner = []
for i in range(r):
    if data[i][0] == -1:
        air_cleaner.append((i, 0))

up_r, up_c = air_cleaner[0]
bottom_r, bottom_c = air_cleaner[1]

for _ in range(t):
    spread()
    top_air_cleaning(up_r, up_c+1, 0, False)
    bottom_air_cleaning(bottom_r, bottom_c+1, 0, False)

result = 2
for i in data:
    result += sum(i)
print(result)
