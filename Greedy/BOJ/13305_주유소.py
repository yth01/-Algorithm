n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
city.pop()

result = 0
m = city[0]
for i in range(len(city)):
    if city[i] < m:
        m = city[i]
    result += m * road[i]

print(result)