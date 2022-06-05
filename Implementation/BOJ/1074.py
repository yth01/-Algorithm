n, r, c = map(int, input().split())

def Divide(n, r, c):
    if n == 0:
        return 0
    return 2 * (r % 2) + (c % 2) + 4 * Divide(n-1, r//2, c//2)

print(Divide(n, r, c))
