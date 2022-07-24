from copy import deepcopy

n = int(input())

max_data = [list(map(int, input().split()))]
min_data = deepcopy(max_data)
temp = [0] * 3
for i in range(1, n):
    a, b, c = map(int, input().split())
    temp[0] = a + max(max_data[0][0], max_data[0][1])
    temp[1] = b + max(max_data[0][0], max_data[0][1], max_data[0][2])
    temp[2] = c + max(max_data[0][1], max_data[0][2])
    for i in range(3):
        max_data[0][i] = temp[i]

    temp[0] = a + min(min_data[0][0], min_data[0][1])
    temp[1] = b + min(min_data[0][0], min_data[0][1], min_data[0][2])
    temp[2] = c + min(min_data[0][1], min_data[0][2])
    for i in range(3):
        min_data[0][i] = temp[i]
    
print(max(max_data[-1]), min(min_data[-1]))
