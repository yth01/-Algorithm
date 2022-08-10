from math import sqrt

n = int(input())
data = [True] * (n+1)

for i in range(2, int(sqrt(n))+1):
    if data[i] == True:
        j = 2
        while i * j <= n:
            data[i*j] = False
            j += 1

prime_numbers = []
for i in range(2, n+1):
    if data[i] == True:
        prime_numbers.append(i)

cnt = 0
end = 0
interval_sum = 0
length = len(prime_numbers)
for start in range(length):
    while interval_sum < n and end < length:
        interval_sum += prime_numbers[end]
        end += 1
    if interval_sum == n:
        cnt += 1
    interval_sum -= prime_numbers[start]

print(cnt)
