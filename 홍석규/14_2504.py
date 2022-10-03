import sys
sys.stdin = open("input.txt","r")
# 14. https://www.acmicpc.net/problem/17608 : 막대기
input = sys.stdin.readline

n = int(input())
stick_list = [int(input()) for _ in range(n)]

#막대기 리스트에서 pop
# pop 해둔 막대기는 X로 저장
x = stick_list.pop()
s_list = []
while True:
    if len(stick_list) == 0:
        break
    y = 0
    # y = stick_list.pop()
    
    if len(s_list) == 0:
        y = stick_list.pop()
        if y > x:
            s_list.append(y)
        
    elif len(stick_list) != 0:
        y = stick_list.pop()
        if y > x and y > s_list[-1]:
            s_list.append(y)
      
   

print(len(s_list)+1)    


        
    





# 막대기 리스트에서 Pop
# pop한 막대기가 X보다 작거나 같다면 버리고, 크면 append 다른 리스트
# 
# 막대기에서 계속 pop
# 만약 X보다 크고 다른 리스트의 마지막 막대보다 크다면 append
# 다른 리스트 총 개수 확인



        
    

    