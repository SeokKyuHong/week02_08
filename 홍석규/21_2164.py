import sys
from collections import deque
sys.stdin = open("input.txt","r")
# 21. https://www.acmicpc.net/problem/2164 : 카드2
input = sys.stdin.readline

n = int(input())
list_n = []
for i in range(1, n+1):
    list_n.append(i)
arr = deque(list_n)


# 첫번째 liftpop, 두번째 liftpop 후 Push, 세번째 liftpop...
queue = []

while len(arr) > 1:
    arr.popleft()
    arr.rotate(-1)
print(*arr)



