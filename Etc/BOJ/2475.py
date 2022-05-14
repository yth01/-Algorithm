data = list(map(int, input().split()))

def square(lst):
    return list(map(lambda x: x ** 2, lst))

print(sum(square(data))%10)
