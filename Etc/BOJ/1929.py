import math

m, n =map(int, input().split())

data = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if(data[i] == True):
        j = 2
        while i*j <= n:
            data[i*j] = False
            j += 1

data[1] = False
for i in range(m, n+1):
    if data[i]:
        print(i)
