import itertools

n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))

nCr = list(itertools.combinations(cards, 3))
data = sorted(list(map(lambda x:sum(x), nCr)))

result = 0
for i in data:
    if i > m:
        break
    else:
        result = i
print(result)
