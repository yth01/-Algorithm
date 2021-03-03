n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.reverse()

count = 0
a = data[0]
for i in data[1:]:
    if a <= i:
        a -= 1
        count += i - a
    else:
        a = i

print(count)