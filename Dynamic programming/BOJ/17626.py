INF = int(1e9)

n = int(input())
d = [0, 1]

for i in range(2, n+1):
    min_value = INF
    j = 1
    while j**2 <= i:
        min_value = min(min_value, d[i - (j**2)])
        j += 1
    d.append(min_value + 1)

print(d[n])
