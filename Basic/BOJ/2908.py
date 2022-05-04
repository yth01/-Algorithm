data = input().split()

data = list(map(lambda x:int(x[::-1]), data))

print(data[0] if data[0] > data[1] else data[1])
