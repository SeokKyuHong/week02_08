import sys
sys.stdin = open("input.txt","r")
# 07. https://www.acmicpc.net/problem/10828 : 스택
input = sys.stdin.readline

N = int(input())

stack_list = []

for i in range(N):
    element = input().split()

    if element[0] == 'push':
        stack_list.append(int(element[1]))

    elif element[0] == 'pop':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list.pop())
    elif element[0] == 'size':
        print(len(stack_list))
    elif element[0] == 'empty' :
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif element[0] == 'top' :
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])

