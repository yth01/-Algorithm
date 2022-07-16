import sys
import heapq

def input():
    return sys.stdin.readline()[:-1]

n = int(input())
heap = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        if len(heap) == 0:
            print(0)
        else:
            a, b = heapq.heappop(heap)
            print(b)
    else:
        heapq.heappush(heap, (abs(cmd), cmd))
