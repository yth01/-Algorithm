def DividePaper(r, c, n):
    num = data[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if data[i][j] != num:
                # Divide paper
                for k in range(3):
                    for l in range(3):
                        DividePaper(r+k*(n//3), c+l*(n//3), n//3)
                return 
    
    if num == -1:
        result[0] += 1
    elif num == 0:
        result[1] += 1
    elif num == 1:
        result[2] += 1

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
result = [0, 0, 0]

DividePaper(0, 0, n)

for i in result:
    print(i)
