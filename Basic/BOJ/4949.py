import re

data = []
while True:
    sentence = input()
    if sentence == '.':
        break
    else:
        data.append(sentence)

data = list(map(lambda x:''.join(re.findall(r'[\[\]\(\)]', x)), data))

for i in data:
    stack = []
    for j in i:
        if j == '[' or j == '(':
            stack.append(j)
        elif j == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append('exit')
                break
        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append('exit')
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
