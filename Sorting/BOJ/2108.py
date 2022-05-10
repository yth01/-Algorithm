from collections import Counter

def getMode(data):
    c = Counter(data)
    mode = c.most_common()
    mode.sort(key=lambda x:(-x[1], x[0]))
    if len(mode) > 1:
        if mode[0][1] == mode[1][1]:
            return mode[1][0]
        else:
            return mode[0][0]
    else:
        return mode[0][0]

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

print(round(sum(data)/n))
print(data[n//2])
print(getMode(data))
print(max(data)-min(data))
