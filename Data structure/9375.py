from collections import Counter

T = int(input())
for _ in range(T):
    n = int(input())

    data = []
    for _ in range(n):
        a, b = input().split()
        data.append(b)
    count = Counter(data)

    result = 1
    for key in count:
        result *= count[key] + 1
    print(result - 1)
