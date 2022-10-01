#push=( pop =) 총 0 이되면 yes 안에 남아있으면 no
import sys
n= int(input())
a = [sys.stdin.readline().strip() for i in range(n)]

for i in a:
    print(i)
    print(type(i))
    
# for i in range(n):
#     a = input()
#     print(type(a))
    
#     vps=[]
#     for order in a:
#         print(order)
#         if order =='(':
#             vps.append(order)
            
#         elif order==')' : 
        
#             vps.pop()
#         else:
#             print("no")
#             break
    
# if not vps:
#     print("yes")
# else:
#     print("no")


