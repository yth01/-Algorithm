from  collections import deque

num = int(input())
for _ in range(num):
    queue = deque()
    idx_queue = deque()
    n, index = map(int, input().split())
    data = list(map(int, input().split()))
    for i in data:
        queue.append(i)
        idx_queue.append(0)

    idx_queue[index] = 1
    
    order = 0
    while True:
        if queue[0] == max(queue):
            order += 1
            if idx_queue[0] == 1:
                print(order)
                break
            else:
                queue.popleft()
                idx_queue.popleft()
        else:
            queue.append(queue.popleft())
            idx_queue.append(idx_queue.popleft())
