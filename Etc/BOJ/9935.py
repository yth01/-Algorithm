data = str(input())
bomb = str(input())

last_bomb = bomb[-1]
len_bomb = len(bomb)
stack = []
for s in data:
    stack.append(s)
    if s == last_bomb and ''.join(stack[-len_bomb:]) == bomb:
        del stack[-len_bomb:]

result = ''.join(stack)
if result == '':
    print("FRULA")
else:
    print(result)
