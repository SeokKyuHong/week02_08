import sys
from collections import deque
sys.stdin = open("input.txt","r")
# 22. https://www.acmicpc.net/problem/11866 : 요세푸스 문제 0
input = sys.stdin.readline

# 1 ~ n 번까지 있는 사람 
# k(3) 건너서 죽이고 죽이는 순서가 답

n, k = map(int, input().split())

list_n = []
for i in range(1, n+1):
    list_n.append(i)
arr = deque(list_n)


result = []
while len(arr) > 0: # 1까지 반복하고 0이면 종료!!!
    for i in range(k):
        if i == k-1:
            result.append(arr.popleft())

        else:
            arr.rotate(-1)

a = ', '.join(map(str, result))

print(f'<{a}>')            
























# #리스트의 개수(n), 건너 뛰는 범위(k)
# n, k = map(int, input().split())

# n_list = deque([])
# for i in range(1, n+1):
#     n_list.append(i)
# # queue 데이터를 넣기 위한 빈 리스트
# queue = []
# while True:
#     for _ in range(k-1): # 맨 앞에 요소를 뒤로 push하는데, k-1만큼 넘긴다.
#         n_list.append(n_list.popleft())
    
#     queue.append(n_list.popleft()) # k번째는 queue리스트로 넣는다.
#     if len(n_list) == 0: # 리스트가 0이 되면 break
#         break

# # 답에서 제시한 모양대로 만들어준다.
# rere = ', '.join(map(str,queue))
# print(f"<{rere}>")

