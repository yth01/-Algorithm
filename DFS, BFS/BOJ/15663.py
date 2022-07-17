n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
stack = []
visited = [False] * n

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    pre_num = 0
    for i in range(n):
        if not visited[i] and pre_num != data[i]:
            stack.append(data[i])
            visited[i] = True
            pre_num = data[i]
            dfs()
            stack.pop()
            visited[i] = False

dfs()
