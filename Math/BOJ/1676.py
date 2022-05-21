from math import factorial

n = int(input())
result = 0
data = ''.join(reversed(list(str(factorial(n)))))

for i in data:
    if i == '0':
        result += 1
    else:
        break

print(result)
