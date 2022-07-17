n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
stack = []

def dfs(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(start, n):
        stack.append(data[i])
        dfs(i)
        stack.pop()

dfs(0)

