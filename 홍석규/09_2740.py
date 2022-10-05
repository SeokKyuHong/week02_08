import sys
sys.stdin = open("input.txt","r")
# 09. https://www.acmicpc.net/problem/2740 : 행렬 곱셈
input = sys.stdin.readline

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int, input().split())))

axb = [[0]*k for _ in range(n)]
print(axb)
for row in range(n):
    for col in range(k):
        e = 0
        for i in range(m):
            # 0 0 * 0 0 = 1*(-1) >>>> 0 1 * 1 0 = 2 * 0
            e += a[row][i] * b[i][col]
        axb[row][col] = e

for r in axb:
    print(*r)


