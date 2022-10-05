import sys
sys.stdin = open("input.txt","r")
# 06. https://www.acmicpc.net/problem/8983 : 사냥꾼
input = sys.stdin.readline

# m:사냥꾼 수, n: 동물의 수, l: 사정거리 
m, n, l = map(int,input().split())
# 사냥꾼 사로 x 좌표
m_list = list(map(int, input().split()))

# 동물 좌표
x_list = []
for i in range(n):
    x_list.append(list(map(int, input().split())))

x_list.sort(key=lambda x:x[1])

print(x_list) 
count1 = 1
# 사냥꾼 
# 동물의 좌표를 인자로 던져서 
# 좌표 별 사냥이 가능한 범위를 설정
# 해당 x축에 사냥꾼이 있다면 사냥 가능 T
# 없다면 F





