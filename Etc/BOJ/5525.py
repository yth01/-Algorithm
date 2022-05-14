''' 50 score  
n = int(input())
m = int(input())
s = list(input())

seq = "I"
for i in range(n):
    seq += "OI"

cnt = 0
for i in range(len(s)-(len(seq)-1)):
    slicing_seq = ''.join(s[i:i+len(seq)])
    if seq == slicing_seq:
        cnt += 1

print(cnt)
'''

n = int(input())
m = int(input())
s = list(input())

data = []
for i in range(len(s)):
    if s[i] == 'I':
        data.append(i)

cnt = 0
result = 0
for i in range(1, len(data)):
    if data[i] - data[i-1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= n:
        result += 1

print(result)
