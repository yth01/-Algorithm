count = 1
while 1:
    L, P, V = map(int, input().split())
    result = 0

    if L == 0 and P == 0 and V == 0:
        break
    else:
        while 1:
            if V > P:
                V -= P
                result += L
            else:
                if V < L:
                    result += V
                else:
                    result += L
                break

    print("Case %d: %d" %(count, result))
    count += 1