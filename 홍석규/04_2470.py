import sys
sys.stdin = open("input.txt","r")
# 04. https://www.acmicpc.net/problem/2470 : 두 용액
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split(' ')))
n_list.sort()
# combi = list(itertools.combinations(n_list, 2))
# result = []
# for i in combi:
#     result.append(abs(i[0] + i[1]))

# min1 =min(result)

# for i, x in enumerate(result):
#     if min1 == x:
#         result_1 = ' '.join(map(str, combi[i]))
#         print(result_1) 

pl = 0 # 처음 점
pr = n-1 # 끝 점

# 두 포인트를 더한 절대값
hold = abs(n_list[pl]+n_list[pr])
# 답을 출력하기 위한 변수
result = (n_list[pl], n_list[pr])

# pl과 pr이 만날때 까지 반복
while pl < pr:
    sum = n_list[pl] + n_list[pr] # 1. 양끝점을 더한 값
    if hold > abs(sum): # 2. 처음 더한 값 > 새로 더한 값          
        hold = abs(sum)   
        result = n_list[pl], n_list[pr]
        if hold == 0:
            break
    if sum < 0:
        pl += 1
    else:
        pr -= 1


print(result[0],result[1])


        
    

