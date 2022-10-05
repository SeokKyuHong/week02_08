import sys
sys.stdin = open("input.txt","r")
# 08. https://www.acmicpc.net/problem/1629 : 곱셈
input = sys.stdin.readline

a, b, c = map(int, input().split())

def gop(a, b):
    if b == 1:
        return a % c
        
    t = gop(a, b//2)

    if b%2 == 0:
        return t * t % c
    else:
        return t * t * a % c

# 짝수일때 
# a ** b % c  = ((a ** b//2) * (a ** b//2)) % c

print(gop(a, b))

























#-----------------------------------------
# a, b, c = map(int, input().split())
# def gop(a, b):
#     if b == 1:
#         return a%c 

#     x = gop(a, b//2)

#     if b%2 == 1: # 홀수이면
        
#         return x * x * a % c
#     else:
        
#         return x * x % c
        
# print(gop(a,b))