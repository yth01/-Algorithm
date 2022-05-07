n = int(input())
data = [int(input()) for _ in range(n)]

stack = []
for i in data:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))
