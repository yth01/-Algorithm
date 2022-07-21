n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
triangle.reverse()

for row in range(n-1):
    for col in range(n - row - 1):
        triangle[row+1][col] += max(triangle[row][col], triangle[row][col+1])

print(triangle[n-1][0])
