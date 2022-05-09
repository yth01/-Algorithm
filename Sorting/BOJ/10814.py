n = int(input())

data = []
for _ in range(n):
    data.append(input().split())
data.sort(key=lambda x:int(x[0]))

for i in data:
    print(f"{i[0]} {i[1]}")
