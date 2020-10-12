a = list(map(int, input().split()))
day = 1
while ( day % a[0] != 0 or day % a[1] != 0 or day % a[2] != 0):
    day += 1
print(day)