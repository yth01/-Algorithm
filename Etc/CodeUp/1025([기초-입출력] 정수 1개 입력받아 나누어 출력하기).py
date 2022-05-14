a = list(map(int, input()))
b = 10**(len(a)-1)

for i in a:
    print("[%d]" %(i*b))
    b //= 10

