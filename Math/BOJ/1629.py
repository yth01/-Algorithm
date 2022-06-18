a, b, c = map(int, input().split())


def Divide(a, b):
    if b == 1:
        return a % c

    temp = Divide(a, b//2)
    if b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c


result = Divide(a, b)
print(result)
