import sys
sys.stdin = open("input.txt","r")
# 09. https://www.acmicpc.net/problem/10830 : 행렬 제곱
input = sys.stdin.readline

n, b = map(int, input().split())

# 행렬을 a, 제곱할 수를 z 라고 하면
def line(a, b):
    if b == 1:
        return a%1000
    
    x = line(a, b//2)

    if b%2 == 1: # 홀수일때
        return x * x * a // 1000
    else: 
        return x * x // 1000

print(line(n,b))



