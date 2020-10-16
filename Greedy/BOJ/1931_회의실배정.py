'''
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    data[i].append(data[i][1] - data[i][0])
data.sort(key=lambda x:[x[2], x[0]])

start = lambda x:x[0]
end = lambda x:x[1]

result = []
count = 0
for i in range(len(data)):
    box = []
    same_value = 0
    start_value = start(data[i])
    end_value = end(data[i])
    for j in range(start_value, end_value+1):
        box.append(j)
    for j in box:
        for k in result:
            if k == j:
                same_value += 1
    if same_value < 2:
        count += 1
        for j in box:
            result.append(j)
print(count)
'''

import sys
n = int(sys.stdin.readline().rstrip())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x:[x[1], x[0]])

count = 0
start = 0
for i in data:
    if i[0] >= start:
        start = i[1]
        count += 1
print(count)