t = int(input())
n = []
for i in range(t):
    n.append(int(input()))

for i in n:
    d = [0] * 41

    d[1] = 1
    d[2] = 1
    for j in range(3, i+1):
        d[j] = d[j-1] + d[j-2]

    if i == 0:
        print(1, 0)
    else:
        print(d[i-1], d[i])
