n = int(input())
data = sorted(map(float, input().split()), reverse=True)

max_num = data[0]
for i in range(n):
    data[i] = data[i]/max_num*100

print(sum(data)/len(data))
