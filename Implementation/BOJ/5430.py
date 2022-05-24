from collections import deque 
import sys 
def input():
    return sys.stdin.readline()[:-1]

T = int(input()) 
for _ in range(T): 
    p = list(input()) 
    n = int(input()) 
    data = deque(input()[1:-1].split(',')) 
    
    if n == 0: 
        data = deque() 
    
    flag = True 
    rev = 0
    for i in p: 
        if i == 'R':
            rev += 1
        if i == 'D': 
            if len(data) == 0: 
                print("error") 
                flag = False 
                break 
            else:
                if rev % 2 == 0:
                    data.popleft()
                else:
                    data.pop() 

    if flag:
        if rev % 2 == 0:
            print('[' + ','.join(data) + ']')
        else:
            data.reverse()
            print('[' + ','.join(data) + ']')
