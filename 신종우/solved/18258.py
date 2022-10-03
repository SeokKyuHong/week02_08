import sys


input = sys.stdin.readline

n = int(input())

queue = [None]
f=0
r=0

for _ in range(n):
    row = input().split()
    if row[0] == "push":
        queue.append(int(row[1]))
        f = len(queue)-1

    elif row[0] == "pop":
        if f!=r:
            r+=1
            v = queue[r]
            queue[r] = None

            print(v)
        else:
            print(-1)
        
    elif row[0] == "size":
        size = f-r
        print(size)

    elif row[0] == "empty":
        if f==r:
            print(1)
        else:
            print(0)

    elif row[0] == "front":
        if f!=r:
            print(queue[r+1])
        else:
            print(-1)
        
    elif row[0] == "back":
        if f!=r:
            print(queue[f])
        else:
            print(-1)
