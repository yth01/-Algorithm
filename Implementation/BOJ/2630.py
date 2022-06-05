def DividePaper(r, c, n):
    num = data[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if num != data[i][j]:
                for k in range(2):
                    for l in range(2):
                        DividePaper(r+k*(n//2), c+l*(n//2), n//2)
                return
    
    if num == 0:
        result[0] += 1
    elif num == 1:
        result[1] += 1

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = [0, 0]

DividePaper(0, 0, n)

for i in result:
    print(i)
