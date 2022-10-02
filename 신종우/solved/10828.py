n = int(input())

stack = [None]*10001
stack_ptr = 0

res=[]
for _ in range(n):
    row = list(input().split())

    if row[0]=="push":
        stack_ptr+=1
        stack[stack_ptr]=int(row[1])

    elif row[0]=='pop':
        v = stack[stack_ptr]

        res.append(v if stack_ptr>0 else -1)
        if stack_ptr>0:
            stack[stack_ptr]=None
            stack_ptr-=1
  
    elif row[0]=='size':
        res.append(stack_ptr)
        
    elif row[0]=='empty':
        res.append(1 if stack_ptr==0 else 0)
  
    elif row[0]=='top':
        res.append(stack[stack_ptr] if stack_ptr > 0 else -1)

for r in res:
    print(r)
    

