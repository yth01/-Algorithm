S = list(map(int, input()))

count_0 = 0
count_1 = 0
left = 2
for i in S:
    if left == i:
        continue
    left = i

    if i == 0:
        count_0 += 1
    else:
        count_1 += 1

print(count_0 if count_0 < count_1 else count_1)

'''
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
'''

