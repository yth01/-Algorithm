a, b = map(bool, map(int, input().split()))
c = int((not a) and (not b))
print(c)