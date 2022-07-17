n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
stack = []

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for i in data:
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()

dfs()
