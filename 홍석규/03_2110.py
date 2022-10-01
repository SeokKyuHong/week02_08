import sys
sys.stdin = open("input.txt","r")
# 03. https://www.acmicpc.net/problem/2110 : 공유기 설치
input = sys.stdin.readline

N, C = map(int, input().split()) # N: 집 개수, C : 와이파이 개수
x = list(int(input()) for _ in range(N)) # 집의 위치 리스트

#퀵 정렬(x자체를 수정)
# def qsort(arr, start, end):
#     pl = start
#     pr = end
#     pivot = arr[(start + end)//2]
#     while pl <= pr:
#         while arr[pr] > pivot : pr -= 1
#         while arr[pl] < pivot : pl += 1
#         if pl <= pr:
#             arr[pr], arr[pl] = arr[pl], arr[pr]
#             pr -= 1
#             pl += 1
#     if pl < end :qsort(arr, pl, end)
#     if pr > start : qsort(arr, start, pr)

# qsort(x, 0, len(x)-1)
# 정렬 완료 [1,2,4,8,9]
x.sort()

pl = 1 # 최소 gap
pr = x[-1] - x[0] # 최대 gap

result = 0

while (pl <= pr):
    pivot = (pr + pl) // 2 # gap
    count1 = 1 # 무조건 처음에 하나 설치하고 시작하기 때문에
    last_C = x[0]
    for i in range(1, len(x)):
        if x[i] >= last_C + pivot:
            count1 += 1
            last_C = x[i]
    if count1 >= C:
        pl = pivot + 1
        result = pivot            
    else:
        pr = pivot -1
print(result)

   

