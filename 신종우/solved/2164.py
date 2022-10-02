n = int(input())

queue = [x for x in range(1,n+1)]
f = 0
flag = False
while True:
  if f==len(queue)-1:
    print(queue[f])
    break
  
  if flag:
    queue.append(queue[f])

  queue[f]= None
  
  flag = not flag
  f+=1
