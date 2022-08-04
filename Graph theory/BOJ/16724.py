def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


n, m = map(int, input().split())
data = []
for _ in range(n):
  data.append(list(input()))
parent = [i for i in range(n*m)]
command = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

for idx in range(n*m):
  r = idx // m
  c = idx % m
  cmd = data[r][c]
  nr = r + command[cmd][0]
  nc = c + command[cmd][1]
  if 0 <= nr < n and 0 <= nc < m:
    next_idx = nr*m + nc
    union_parent(parent, idx, next_idx)

cnt = 0
visited = dict()
for idx in range(n*m):
    if find_parent(parent, idx) not in visited:
        visited[idx] = True
        cnt += 1
print(cnt)
