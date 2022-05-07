import sys
n = int(sys.stdin.readline().rstrip())

stack = []
data = 0
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:
        data = cmd[1]
        cmd = cmd[0]
    else:
        cmd = cmd[0]

    if cmd == 'push':
        stack.append(data)
    elif cmd == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif cmd == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
