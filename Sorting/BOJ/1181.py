n = int(input())
data = []
for _ in range(n):
    data.append(input())

data = list(set(data))
data = sorted(data)
data = sorted(data, key=lambda x:len(x))

for i in range(len(data)):
    print(data[i])
