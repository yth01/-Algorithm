t = int(input())
data = []
for _ in range(t):
    data.append(input())

for i in data:
    r, s = i.split()
    r = int(r)
    s = list(s)

    result = ""
    for i in s:
        result += i * r

    print(result)    
