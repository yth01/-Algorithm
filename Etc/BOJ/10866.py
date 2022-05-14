import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

queue = deque()
data = 0
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:
        data = cmd[1]
        cmd = cmd[0]
    else:
        cmd = cmd[0]

    if cmd == "push_front":
        queue.appendleft(data)
    elif cmd == "push_back":
        queue.append(data)
    elif cmd == "pop_front":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(1 if len(queue) == 0 else 0)
    elif cmd == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
