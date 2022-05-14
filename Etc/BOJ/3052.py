data = []
for _ in range(10):
    data.append(int(input()))

result = []
for i in data:
    result.append(i % 42)

print(len(set(result)))
