count = 1
while 1:
    L, P, V = map(int, input().split())
    result = 0

    if L == 0 and P == 0 and V == 0:
        break

    if V > P:
        result += L * (V // P)
    if V % P < L:
        result += V % P
    else:
        result += L

    print("Case %d: %d" %(count, result))
    count += 1