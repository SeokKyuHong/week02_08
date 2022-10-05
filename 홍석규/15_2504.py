import sys
sys.stdin = open("input.txt","r")
# 15. https://www.acmicpc.net/problem/2504 : 괄호의 값
input = sys.stdin.readline

# stack에 넣는다.
stack = []
# 점수를 계산하는 sum 1로 시작
# 뒤에 열린 괄호가 들어오면서 곱샘을 해주기 때문에
sum = 1
# 괄호가 닫힐때 기존 괄호를 pop하면서 sum을 더해 주기 위한 변수
tmp = 0
# 괄호 데이터를 하나씩 받는다
st=input()
# 문자열의 인덱스 값과 요소를 함께 가져온다. 
for i,v in enumerate(st):
    if v == '(': # 반복문으로 가져온 요소가 열린 괄호일때
        if not stack: # stack에 아무것도 없다면
            stack.append(v) # 가져온 요소를 stack에 더한다.
            sum *= 2 # sum에 2를 곱한다. 
        elif stack[-1] == '(': # 비어있지 않아도 동일
            stack.append(v)
            sum *= 2
        elif stack[-1] == '[': # 열린 괄호가 있다면 동일
            stack.append(v)
            sum *= 2
    elif v == '[': # 위 '(' 와 동일
        if not stack:
            stack.append(v)
            sum *= 3
        elif stack[-1] == '(':
            stack.append(v)
            sum *= 3
        elif stack[-1] == '[':
            stack.append(v)
            sum *= 3
    elif v == ')': # 모양이 맞지 않는 괄호면 tmp를 0으로 만들고 break
        if len(stack) == 0 or stack[-1] == '[':
            tmp = 0
            break
        elif st[i-1] == '(': # 이전 인덱스의 요소와 모양이 맞다면 
            tmp += sum
        stack.pop()
        sum //= 2
        
    elif v == ']':
        if len(stack) == 0 or stack[-1] == '(':
            tmp = 0
            break
        elif st[i-1] == '[': # 이전 인덱스의 요소와 모양이 맞다면
            tmp += sum
        stack.pop()
        sum //= 3

if stack:
    print(0)
else:
    print(tmp)

