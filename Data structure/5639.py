import sys
sys.setrecursionlimit(10**6)

nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break


def postorder(first, end):
    if first > end:
        return
    mid = end + 1
    for i in range(first+1, end+1):
        if nodes[first] < nodes[i]:
            mid = i
            break
   
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(nodes[first])


postorder(0, len(nodes)-1)
