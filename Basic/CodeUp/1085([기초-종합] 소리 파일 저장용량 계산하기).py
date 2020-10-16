a = list(map(int, input().split()))
b = 1
for i in a:
    b *= i
print("%.1f MB" %(b / (8 * 1024 * 1024)))
