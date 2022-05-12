T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    data = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1):
        data[0][i] = i
    for i in range(k+1):
        data[i][1] = 1
    
    for i in range(1, k+1):
        for j in range(2, n+1):
            data[i][j] = data[i][j-1] + data[i-1][j]
    
    print(data[k][n])
