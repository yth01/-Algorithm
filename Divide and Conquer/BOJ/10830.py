import sys
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()[:-1]


N, b = map(int, input().split())
base_matrix = []
for _ in range(N):
    base_matrix.append(list(map(int, input().split())))


def matmul(matrixA, matrixB):
    global N
    result = [[0] * N for _ in range(N)]
    for n in range(N):
        for k in range(N):
            for m in range(N):
                result[n][k] += matrixA[n][m] * matrixB[m][k]
            result[n][k] %= 1000
    return result


def divide(b):
    if b == 1:
        return base_matrix
    else:
        div_matrix = divide(b//2)
        if b % 2 == 0:
            return matmul(div_matrix, div_matrix)
        else:
            return matmul(matmul(div_matrix, div_matrix), base_matrix)


result = divide(b)
for row in result:
    for n in row:
        print(n%1000, end=' ')
    print()
