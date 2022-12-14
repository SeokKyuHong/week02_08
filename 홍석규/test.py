# 1.리스트의 원소만 출력 할때(* 사용)
list_a = [[-1, -2, 6], [-3, -6, 12], [-5, -10, 18]]

print(*list_a)
#결과 : [-1, -2, 6] [-3, -6, 12] [-5, -10, 18]

# 2. 이중 리스트의 원소만 출력할때(반복문, * 사용)
list_a = [[-1, -2, 6], [-3, -6, 12], [-5, -10, 18]]

for i in list_a:
    print(*i)
# 결과 : -1 -2 6
#       -3 -6 12
#       -5 -10 18