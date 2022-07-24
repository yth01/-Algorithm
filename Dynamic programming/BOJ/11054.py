n = int(input())
A = list(map(int, input().split()))
B = list(reversed(A))

increase = [1] * n
decrease = [1] * n

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            increase[i] = max(increase[i], increase[j] + 1)
        if B[j] < B[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = 0
for i in range(n):
    result = max(result, increase[i] + decrease[n-i-1] - 1)
print(result)
