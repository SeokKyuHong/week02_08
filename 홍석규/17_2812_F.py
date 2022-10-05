import sys
sys.stdin = open("input.txt","r")
# 17. https://www.acmicpc.net/problem/2812 : 크게 만들기
input = sys.stdin.readline

n, k = map(int, input().split())
list_n= list(map(int, ''.join(input())))
print(list_n)

stack = []
for i in range(n):
    while k > 0 and stack and stack[-1]< list_n[i]:
        stack.pop()
        k -= 1
    stack.append(list_n[i])
print(stack)

