n = int(input())
data = [int(input()) for _ in range(n)]

bol = True
stack = []
cnt = 1
result= []
for i in data:
    for _ in range(cnt, i+1):
        stack.append(cnt)
        result.append("+")
        cnt += 1
    if stack[-1] == i:
        stack.pop()
        result.append("-")
    else:
        bol = False
        break

if bol == True:
    for i in result:
        print(i)
else:
    print("NO")
