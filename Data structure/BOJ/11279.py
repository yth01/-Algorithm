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
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -cmd)

