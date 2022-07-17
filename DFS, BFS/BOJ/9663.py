n = int(input())

result = 0
row = [0] * n


def check_col_diagonal(r):
    for i in range(r):
        if row[r] == row[i] or abs(row[r] - row[i]) == abs(r - i):
            return False
    return True


def dfs(r):
    global result
    if r == n:
        result += 1
        return

    else:
        for c in range(n):
            row[r] = c
            if check_col_diagonal(r):
                dfs(r+1)


dfs(0)
print(result)
