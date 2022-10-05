import sys
sys.stdin = open("input.txt","r")
# 16. https://www.acmicpc.net/problem/2493 : 탑
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

stack = []
ind = []
# 6 9 5 7 4 
# 6을 입력 받는다
for i in enumerate(n_list):

# 9를 입력 받는다.
# 스택에 요소가 있다면,
    while stack:
        if i[1] < stack[-1][1] :
            ind.append(stack[-1][0]+1)
            stack.append(i)
            break 
# 5를 입력 받는다.
# 스택 확인 후 요소가 있다면 값과 비교
# 가져온 5 < 스택의 top : ind에 해당 top의 0번째 요소 가져오기
        else:
            stack.pop()
        # 스택에 아무것도 없다면 
    if not stack: # 후 다시 스택 체크 / 
        # 스택에 아무것도 없다면 스택에 추가, ind에는 스택에 없다면 0
        stack.append(i) # 6을 넣고
        ind.append(0) # ind에는 스택에 없다면 0
asdf = ''
asdf = ' '.join(map(str,ind))
print(asdf)
# 5는 스택에 어팬드



    

