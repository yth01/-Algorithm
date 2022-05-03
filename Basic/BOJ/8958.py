n = int(input())
data = []
for _ in range(n):
    data.append(list(input()))

for i in data:
    result = 0
    cnt = 0
    for j in i:
        if j == "O":
            cnt += 1
        else:
            cnt = 0
        result += cnt

    print(result)
