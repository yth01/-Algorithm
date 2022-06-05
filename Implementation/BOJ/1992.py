def Divide(r, c, n):
    num = data[r][c]
    if n == 1:
        return str(num)
    result = []
    for i in range(r, r+n):
        for j in range(c, c+n):
            if num != data[i][j]:
                result.append('(')
                result.extend(Divide(r, c, n//2))
                result.extend(Divide(r, c+n//2, n//2))
                result.extend(Divide(r+n//2, c, n//2))
                result.extend(Divide(r+n//2, c+n//2, n//2))
                result.append(')')
                return result
    return str(num)

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, list(input()))))

print(''.join(Divide(0, 0, n)))
