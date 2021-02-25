N, L = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

count = 0
loc = 0
for i in data:
    if loc < i:
        loc = i + L - 1
        count += 1

print(count)