import sys
sys.stdin = open("input.txt","r")
# 15. https://www.acmicpc.net/problem/2504 : 괄호의 값
input = sys.stdin.readline

s = input()

#괄호를 반복문으로 하나씩 받아 stack에 넣을지 말지 결정
# 아무것도 없을때 (가 들어 오면 * 2
# 아무것도 없을때 [가 들어오면 *3
# 