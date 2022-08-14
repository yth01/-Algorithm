def ccw(a, b, c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(b[0]*a[1]+a[0]*c[1]+c[0]*b[1])


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A = [x1, y1]
B = [x2, y2]
C = [x3, y3]
D = [x4, y4]

if ccw(A,B,C)*ccw(A,B,D) <= 0 and ccw(C,D,A)*ccw(C,D,B) <= 0:
    if ccw(A,B,C)*ccw(A,B,D) == 0 and ccw(C,D,A)*ccw(C,D,B) == 0:
        if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
