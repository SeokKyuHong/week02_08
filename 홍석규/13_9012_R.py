import sys
sys.stdin = open("input.txt","r")
# 09. https://www.acmicpc.net/problem/9012 : 괄호
input = sys.stdin.readline

for _ in range(int(input())): # 첫 줄의 케이스를 받고 그 range만큼 괄호를 받는다.
    s = input() # 괄호를 받는다
    stack = [] # 스택으로 쌓을 빈 리스트 
    for c in s: # 괄호 문자열에서 하나씩 확인
        if c == '(': # 열린 괄호면 스택에 추가
            stack.append(c) # 나중에 ')'가 들어올때 빼낼 꺼다.
        elif c == ')': # 닫힌 괄호이면서 
            if len(stack)==0 or stack[-1] != '(':# 리스트가 없거나 스택의 마지막이 ')'이면 
                stack.append(')') # 스택에 추가 하고 
                break # 반복문 나가

            stack.pop() # 스택에 ( 열린괄호가 있으면 pop

    # 스택에 리스트가 짝으로 있다면 YES출력, 없거나 하나면 NO출력
    if len(stack) == 0:
        print('YES')
    else:
        print('NO') 
            
# t = int(input())
# for _ in range(t):
#     ps = input()
#     stack1 = []
#     for i in ps :
#         if i == '(':
#             stack1.append(i)
#         elif i == ')':
#             if len(stack1) == 0 or stack1[-1] != '(':
#                 stack1.append(i)
#                 break
        
#             stack1.pop()

#     if len(stack1) == 0:
#         print("YES")
#     else:
#         print("NO")