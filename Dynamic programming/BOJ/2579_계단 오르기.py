n = int(input())
score = []
for i in range(n):
    score.append(int(input()))
score.append(0)
score.append(0)
'''
score = [] * 301
for i in range(n):
    score[i] = int(input())
'''

d = [0] * 301
d[0] = score[0]
d[1] = score[0] + score[1]
d[2] = score[2] + max(score[0], score[1])

for i in range(3, n):
    d[i] = score[i] + max(score[i-1] + d[i-3], d[i-2])

print(d[n-1])