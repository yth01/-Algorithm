import sys

def input():
    return sys.stdin.readline()[:-1]

s1 = input()
s2 = input()
rows = len(s1)+1
cols = len(s2)+1
matrix = [[0] * cols for _ in range(rows)]

for i in range(1, rows):
    for j in range(1, cols):
        if s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])
