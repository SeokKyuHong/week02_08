n = int(input())

stack = [None] * (n+1)
stack_ptr = 0
sum = 0

for _ in range(n):
    row = input()
    if row=='0':
        if stack_ptr>0:
            v = stack[stack_ptr]
            stack[stack_ptr]=None
            stack_ptr -= 1
            sum -= v

    else:
        stack_ptr+=1
        v =int(row)
        stack[stack_ptr]=v
        sum+=v
  
print(sum)