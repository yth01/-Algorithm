L = int(input())
word = list(input())

result = 0
cnt = 0
for i in word:
    result += (ord(i)-96) * (pow(31, cnt))
    cnt += 1

print(result % 1234567891)
