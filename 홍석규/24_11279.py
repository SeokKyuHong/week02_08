import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt","r")
# 24. https://www.acmicpc.net/problem/11279 : 최대힙
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    
    if x == 0 :
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else: 
        heappush(heap, (-x, x))
    
        