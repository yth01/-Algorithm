n, m = map(int, input().split())
truth_people = set(list(map(int, input().split()))[1:])

parties = []
for i in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

for i in range(m):
    for party in parties:
        flag = False
        for people in party:
            if people in truth_people:
                flag = True
                break
        if flag:
            for people in party:
                truth_people.add(people)

result = 0
for party in parties:
    flag = True
    for people in party:
        if people in truth_people:
            flag = False
    if flag:
        result += 1
print(result)
