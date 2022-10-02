n = int(input())
stack = [None] * (n+1)
stack_ptr = 0


cnt =0
prev=0

for _ in range(n):
  stack_ptr+=1
  stack[stack_ptr] = int(input())

for _ in range(n):
  v = stack[stack_ptr]
  stack_ptr-=1

  if v>prev:
    cnt+=1
    prev = v
    
print(cnt)  
    
