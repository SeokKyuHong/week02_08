import sys
sys.stdin = open("input.txt","r")
# 07. https://www.acmicpc.net/problem/2630 : 색종이 만들기
input = sys.stdin.readline

n = int(input())
s_list = [list(map(int,input().split())) for _ in range(n)]

white = 0
blue = 0
def divide(x, y, N):
    global white, blue
    #체크를 x, y 기준으로 한다.
    check = s_list[x][y]
    #이중반복문 처음은 x를 기준으로 y를 확인
    for i in range(x, x+N):
        for j in range(y, y+N):
            # if 처음에 받은 체크의 x,y가 반복문을 돌릴때마다 체크되는 x,y가 다르다면
            if check != s_list[i][j]:
                divide(x, y, N//2)#1사분y
                divide(x, y+(N//2), N//2)#3사분면
                divide(x+(N//2), y, N//2)#2사분면
                divide(x+(N//2), y+(N//2), N//2)#4사분면
                return
    #만약에 체크가 0,0: 이라면, white +=1
    # 아니라면(1,1)이라면: blue +=1
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

divide(0, 0, n)
print(white)
print(blue)









