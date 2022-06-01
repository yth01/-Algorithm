n = int(input())

data = list(map(int, input().split()))
sort_data = sorted(list(set(data)))

dic = {}
for i in range(len(sort_data)):
    dic[sort_data[i]] = i 
   
for i in data:
    print(dic[i], end=' ')
