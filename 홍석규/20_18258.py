import sys
from collections import deque
sys.stdin = open("input.txt","r")
# 20. https://www.acmicpc.net/problem/18258 : 큐2
input = sys.stdin.readline
n = int(input())
queue = deque([]*2000000)
for i in range(n):
    check = input().split()
    if check[0] == 'push':
        queue.append(int(check[1]))
        
    elif check[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
            
    elif check[0] == 'size':
        print(len(queue))
    elif check[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif check[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif check[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)