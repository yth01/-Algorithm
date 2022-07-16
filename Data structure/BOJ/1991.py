n = int(input())

tree =  {}
for i in range(n):
    a, b, c = map(str, input().split())
    tree[a] = (b, c)

preorder = []
inorder = []
postorder = []


def dfs(v):
    preorder.append(v)
    left = tree[v][0]
    if left != '.':
        dfs(left)
    inorder.append(v)
    right = tree[v][1]
    if right != '.':
        dfs(right)
    postorder.append(v)


dfs('A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
