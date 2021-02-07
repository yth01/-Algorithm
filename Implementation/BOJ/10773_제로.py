k = int(input())
data = []
for _ in range(k):
    data.append(int(input()))

stack = []
for i in range(k):
    if data[i] == 0:
        stack.pop()
    else:
        stack.append(data[i])

print(sum(stack))