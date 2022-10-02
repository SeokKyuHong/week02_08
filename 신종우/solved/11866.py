n,k = map(int,input().split())
arr = [x for x in range(1,n+1)]
res = []
cnt = 0
f = 0
while True:
  if len(arr) == f:
    break
  v = arr[f]
  if cnt < k-1:
    arr.append(v)
  else:
    res.append(v)

  arr[f] =None
    
  f+=1
  cnt += 1
  cnt %= k
  print()

print(f'<{", ".join(map(str, res))}>')
