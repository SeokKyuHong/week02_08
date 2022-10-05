
import sys
sys.stdin = open("input.txt","r")
# 08. https://www.acmicpc.net/problem/10773 : 제로
input = sys.stdin.readline

k = int(input())
k_list = []
for i in range(k):
    n = int(input())
    if n == 0:
        k_list.pop()
    else:
        k_list.append(n)
    
    
        
        
print(sum(k_list))