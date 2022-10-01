import sys
sys.stdin = open("input.txt","r")
# 01. https://www.acmicpc.net/problem/1920 : 수 찾기
sys.setrecursionlimit(10**5)
N = int(input())# N배열의 개수
N_list = list(map(int, input().split()))# N배열
M = int(input()) # M배열의 개수
M_list = list(map(int, input().split()))# M배열

# # N_list와 M_list의 element를 비교하는 함수
# def asdf(list, element):
#     for check in list: # N_list의 element와 M_list의 element를 하나씩 비교, 맞으면 1, 틀리면 0
#         if check == element:
#             return 1
#     return 0

# # M_list의 element를 하나씩 비교하여 함수로 던짐
# for M_element in M_list:
#     print(asdf(N_list, M_element))
    
# 위와같이 선형탐색으로 하면 시간초과가 뜸
# 정렬 후 이분탐색으로 진행 해야함

# 퀵 정렬 재귀함수 
def quick_sort(arr, left, right):
    pl = left # 첫번째 index 를 pl로 할당
    pr = right # 마지막 index를 pr로 할당 
    p = arr[(left+right) // 2] # 위 두개로 pivot을 계산해 리스트의 가운데 element를 p에 할당
    
    while pl <= pr: # 양끝점 두개가 붙꺼나 같아질때까지 반복해라
        while arr[pl] < p : pl += 1 # 리스트 제일 왼쪽 요소가 p보다 작은 것을 찾을때까지 pivot으로 이동, 발견하면 stop
        while arr[pr] > p : pr -= 1 # 리스트 제일 오른쪽 요소가 p보다 큰 것을 찾을때까지 pivot으로 이동, 발견하면 stop
        if pl <= pr : # 만약 이동하다가 pl과 pr이 만나거나 교차하게 되면
            arr[pl], arr[pr] = arr[pr], arr[pl] # pl과 pr의 위치를 바꿔라
            pl += 1 # 바뀐 pl은 +1
            pr -= 1 # 바뀐 pr은 -1
    # 교차된 후
    if left < pr : quick_sort(arr, left, pr) # 처음 pl(left)이 pr보다 작다면 처음 pl과 새로운 pr을 기준으로 다시 리스트를 만들어 재귀
    if pl < right : quick_sort(arr, pl, right) # 처음 pr(right)이 pl보다 크다면 처음 pr과 새로운 pl을 기준으로 다시 리스트를 만들어 재귀
    
quick_sort(N_list, 0, len(N_list)-1) # 함수로 보낼 element는 리스트, 0, 리스트의 길이-1
                                    # 0: 리스트의 첫번째 index, 리스트의 길이-1: 리스트의 마지막 index
# print(N_list)

# 이분법 반복문함수
def binary_search(sort_list, key):
    pl = 0 # 리스트의 처음을 pl으로 잡는다.
    pr = len(sort_list)-1 # 리스트의 마지막을 pr로 잡는다.

    while True:
        pc = (pl+pr) // 2 # 중간 수를 pc로 잡는다.(pr//2 로 하지 않은 이유는 아래를 보면 알 수 있다.)
        if sort_list[pc] == key: # sort_list의 인덱스가 pc인 값과 Key가 같다면 바로찾음
            return 1
        elif sort_list[pc] < key: # sort_list의 인덱스가 pc인 값이 key보다 작다면 pc+1을 pl로 만든다.
            pl = pc + 1
        else: # sort_list의 인덱스가 pc인 값이 key보다 크다면 pc11을 pr로 만든다.
            pr = pc - 1
        
        if pl > pr: # pl과 pr이 교차되면 반복문 탈출
            break
    return 0 # 위 조건을 모두 만족 못한다면 없는거임


 # 퀵 정렬 방식으로 N_list를 오름차순으로 정렬한다.
for element in M_list: # 처음 Input으로 받은 M_list의 element를 뽑아내 정렬된 sort_N 리스트를 이분법으로 조회한다.
    print(binary_search(N_list, element))# 이분법 함수로 보냄
    
