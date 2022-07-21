def divide(n, e):
    if e == 1:
        return n % num
    
    if e % 2:
        return n * divide(n, e-1) % num
    else:
        temp = divide(n, e//2)
        return temp * temp % num


m = int(input())
num = 1000000007
result = 0

for _ in range(m):
    n, s = map(int, input().split())
    result += s * divide(n, num-2) % num

print(result % num)
