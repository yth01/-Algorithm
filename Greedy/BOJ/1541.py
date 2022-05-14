exp = input().split('-')

result = sum(list(map(int, exp[0].split('+'))))
for i in exp[1:]:
    total = sum(list(map(int, i.split('+'))))
    result -= total

print(result)
