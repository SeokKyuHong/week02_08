def b_search(arr, v, start, end):
    if start>end:
        return -1

    mid = (start+end)//2
    
    if arr[mid]<v:
      return b_search(arr, v, mid+1, end)
    if arr[mid]>v:
      return b_search(arr, v, start, mid-1)
    return mid  
  

n = int(input())
xs = list(map(int,input().split()))
sorted(xs, 0, len(xs)-1)
m = int(input())
ys = list(map(int,input().split()))

res = []

for y in ys:
  res.append(0 if b_search(xs, y,0,len(xs)-1)==-1 else 1)

for r in res:
  print(r)
