n = int(input())
for _ in range(n):
    data = input()
    stack = []
    for i in data:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append("exit")
                break

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
