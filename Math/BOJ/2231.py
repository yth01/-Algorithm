n = int(input())

result = 0
for i in range(n):
    total = 0
    total += i
    total += sum(map(int, list(str(i))))
    
    if total == n:
        result = i
        break

print(result if result != 0 else 0)
