n = int(input())
score = [0] * 301
for i in range(1, n+1):
    score[i] = int(input())

d = [0] * 301
d[1] = score[1]
d[2] = score[2] + score[1]
d[3] = score[3] + max(score[2], score[1])

for i in range(3, n+1):
    d[i] = score[i] + max(score[i-1]+d[i-3], d[i-2])

print(d[n])
