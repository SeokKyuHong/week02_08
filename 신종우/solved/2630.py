n = int(input())

arr = [ ]
for _ in range(n):
  arr.append(list(map(int, input().split())))

# print(arr)

def solve_paper(r, c, arr,n):
  acc = 0 
  for i in range(n):
      for j in range(n):
          acc += arr[r+i][c+j]
          
  if acc == n**2:
    return (1,0)
  if acc == 0:
    return (0,1)
  
  acc_b, acc_w = 0, 0 

  for i in range(2):
      for j in range(2):
        b,w = solve_paper(r+i*(n//2), c+j*(n//2), arr, n//2)
        acc_b +=b  
        acc_w +=w  
  
  return (acc_b, acc_w)



ans =(solve_paper(0,0,arr,n))
print(ans[1])
print(ans[0])

