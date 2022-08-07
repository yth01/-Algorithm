from bisect import bisect_left, bisect_right

t = int(input())
n = int(input())
a = list(map(int, input().split())) 
m = int(input())
b = list(map(int, input().split()))

A = []
for i in range(n):
    sum_value = a[i]
    A.append(sum_value)
    for j in range(i+1, n):
        sum_value += a[j]
        A.append(sum_value)

B = []
for i in range(m):
    sum_value = b[i]
    B.append(sum_value)
    for j in range(i+1, m):
        sum_value += b[j]
        B.append(sum_value)

A.sort()
B.sort()

cnt = 0
for i in range(len(A)):
    left_idx = bisect_left(B, t-A[i])
    right_idx = bisect_right(B, t-A[i])
    cnt += right_idx - left_idx
print(cnt)
