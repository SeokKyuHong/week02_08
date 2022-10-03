row = list(input())

res = 0 
stack = []

mul_acc = 1
for i, c in enumerate(row):
    if c == '(':
      stack.append(c)
      mul_acc*=2

    if c=='[':
      stack.append(c)
      mul_acc*=3

    if c == ')':
        if len(stack)==0 or stack[-1]!='(':
          res = 0
          break

        if row[i-1]=='(':
          res += mul_acc
        v = stack.pop()
        mul_acc //=2

    if c == ']':
        if len(stack)==0 or stack[-1]!=']':
          res = 0
          break

        if row[i-1]=='[':
          res += mul_acc
        v = stack.pop()
        mul_acc //=3

if len(stack)!=0:
  res = 0

print(res)

  