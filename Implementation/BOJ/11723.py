import sys

def input():
    return sys.stdin.readline()[:-1]

m = int(input())
S = set()
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        cmd = cmd[0]
        if cmd == "all":
            S = set([i for i in range(1, 21)])
        elif cmd == "empty":
            S = set()
    else:
        c, n = cmd[0], int(cmd[1])
        if c == "add":
            S.add(n)
        elif c == "remove":
            S.discard(n)
        elif c == "check":
            print(1 if n in S else 0)
        elif c == "toggle":
            if n in S:
                S.discard(n)
            else:
                S.add(n)
