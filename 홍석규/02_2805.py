import sys
sys.stdin = open("input.txt","r")
# 02. https://www.acmicpc.net/problem/2805 : 나무 자르기

# 나무의 리스트들 중 
# 길이를 비교하여(이분탐색)
# 가장 긴거 1개면 그 나무의 -1
#     두개면 한개씩 -1
# 한개를 자를때마다 카운팅 
# 카운팅이 7(가져갈 나무길이)이 되면 카운팅 리턴 
N, M = map(int, input().split()) # N: 나무 개수, M: 필요한 나무 양(길이)
N_list = list(map(int, input().split())) # N개의 나무리스트

bottom, top = 0, max(N_list) # 절단기 높이와 바닥을 설정한다.

while bottom <= top: # 이분탑색으로 구하기 위해 절단기 높이가 0이 될때 까지 돌린다.
    p = (bottom+top) // 2 # 절단기의 중간 위치를 구한다.
    count1 = 0 # 자른 나무의 양 확인용
    for tree in N_list: # 나무 리스트에서 나무를 하나씩 잘라 count한다.
        if tree >= p:
            count1 += tree - p
    if count1 >= M: # 자른 나무가 필요한 나무보다 크면
        bottom = p + 1 # 더 조금 자르기 위해 절단기를 높힌다.
    else:
        top = p - 1 # 덜 자르기 위해 절단기를 낮춘다.
    
print(top) #최종 절단기의 높이를 구한다. 









