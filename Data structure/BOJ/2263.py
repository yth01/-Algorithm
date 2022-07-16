import sys
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i


def preorder(inFirst, inEnd, postFirst, postEnd):
    if (inFirst > inEnd) or (postFirst > postEnd):
        return

    parent = postorder[postEnd]

    left = position[parent] - inFirst
    right = inEnd - position[parent] 

    print(parent, end=' ')
    preorder(inFirst, inFirst+left-1, postFirst, postFirst+left-1)
    preorder(inEnd-right+1, inEnd, postEnd-right, postEnd-1)


preorder(0, n-1, 0, n-1)
