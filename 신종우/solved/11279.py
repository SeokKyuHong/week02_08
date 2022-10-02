from heapq import heappush,heappop
import sys

input = sys.stdin.readline
arr = []

n = int(input())

for _ in range(n):
  x = int(input())
  if x==0:
      print(heappop(arr)[1] if len(arr)>0 else 0)
  else:
    heappush(arr,(-x,x))
