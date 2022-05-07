while True:
    sentence = input()
    if sentence == '.':
        break
            
    stack = []
    for i in sentence:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append('exit')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append('exit')
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
