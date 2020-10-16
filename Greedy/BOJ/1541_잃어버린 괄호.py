import sys

n = sys.stdin.readline().split('-')

total = 0
a = list(map(int, n[0].split('+')))
total = sum(a)

for i in n[1:]:
    if '+' in i:
        a = list(map(int, i.split('+')))
        total -= sum(a)
    else:
        total -= int(i)

print(total)

