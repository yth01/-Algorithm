from itertools import combinations


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, data):
    global truth_people
    for a, b in combinations(data, 2):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a in truth_people and b in truth_people:
            continue
        else:
            if a in truth_people:
                parent[b] = a
            elif b in truth_people:
                parent[a] = b
            else:
                if a < b:
                    parent[b] = a
                else:
                    parent[a] = b


n, m = map(int, input().split())
truth_people = list(map(int, input().split()))[1:]
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

parties = []
for i in range(m):
    party = list(map(int, input().split()))[1:]
    if len(party) >= 2:
        union_parent(parent, party)
    parties.append(party)

result = 0
for party in parties:
    flag = True
    for x in party:
        if find_parent(parent, x) in truth_people:
            flag = False
            break
    if flag:
        result += 1
print(result)
