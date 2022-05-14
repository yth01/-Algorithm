while True:
    data = sorted(list(map(int, input().split())))
    if sum(data) == 0:
        break
    a, b, c = data

    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        print("right")
    else:
        print("wrong")
