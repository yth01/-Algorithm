import sys
sys.setrecursionlimit(10**6)

n = int(input())
dict = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3
}


def fibo(n):
  if n in dict:
    return dict[n]
  
  if n % 2 == 0:
    dict[n] = (pow(fibo(n//2), 2) + pow(fibo(n//2), 2) + fibo(n//2) * fibo((n-6)//2)) % 1000000007
    return dict[n]
  else:
    dict[n] = (pow(fibo(n//2), 2) + pow(fibo(n//2+1), 2)) % 1000000007
    return dict[n]


print(fibo(n))
