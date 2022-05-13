from itertools import combinations

n, k =map(int, input().split())
n = [0 for _ in range(n)]

print(len(list(combinations(n, k))))
