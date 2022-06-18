from math import factorial

n, r = map(int, input().split())

print(factorial(n)//(factorial((n-r))*factorial(r)))
