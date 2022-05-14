data = ''.join(list(map(str, input().split())))

if data == "12345678":
    print("ascending")
elif data == "87654321":
    print("descending")
else:
    print("mixed")
