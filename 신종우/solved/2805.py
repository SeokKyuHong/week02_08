n, m = map(int, input().split())
arr = sorted(list(map(int,input().split())))

def get_cut_sum(arr,base):
  acc = 0 
  for x in arr:
    if x <= base:
      continue
    acc+=(x-base)

  return acc
  
  # ! 느리다!
  # return sum(map(lambda x:x-base ,filter(lambda x:x >base ,arr)))

start =1
end = arr[-1]

while True:
  base = (start+end)//2

  res = get_cut_sum(arr,base)
  smaller = get_cut_sum(arr,base+1)

  if res>=m and m>smaller:
    print(base)
    break

  if res<m:
    end = base-1
  
  if smaller>=m:
    start = base+1
