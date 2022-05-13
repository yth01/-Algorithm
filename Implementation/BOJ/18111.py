from math import inf

n, m, b = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

result_h = 0
result_time = inf
for i in range(257):
    time = 0
    block = b
    for j in range(n):
        for k in range(m):
            if data[j][k] < i:
                add_block = i - data[j][k]
                block -= add_block
                time += add_block
            elif data[j][k] > i:
                rm_block = data[j][k] - i
                block += rm_block
                time += 2 * rm_block
    if block < 0 or result_time < time:
        continue
    else:
        result_h = i
        result_time = time

print(result_time, result_h)
