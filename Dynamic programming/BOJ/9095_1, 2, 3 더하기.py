t = int(input())
n = []
for i in range(t):
    n.append(int(input()))

for i in n:
    d = [0] * 11
    d[0] = 1
    d[1] = 1
    d[2] = 2
    for j in range(3, i+1):
        d[j] = d[j-1] + d[j-2] + d[j-3]

    print(d[i])
