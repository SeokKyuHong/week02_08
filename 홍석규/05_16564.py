import sys
sys.stdin = open("input.txt","r")
# 05. https://www.acmicpc.net/problem/16564 : 히오스 프로게이머
input = sys.stdin.readline

# 1. n, k값을 받는다. 
n, k = map(int, input().split())
# 2. 캐릭 렙을 받는다.
n_list = [int(input()) for _ in range(n)]

# 3. 리스트에서 가장 작은 값을 bottom으로 사용 
bottom = min(n_list)
# 4. bottom 기준으로 +k 를 top으로 가져간다.
top = bottom + k
# 5. 결과값을 받을 변수
result = 0
while bottom <= top: # 6. 양 끝이 만날때 까지 반복
    pivot = (bottom + top) // 2 # 7. pivot 설정
    sum = 0 # 8. result에 담기 전 일회성 합산 변수
    for i in n_list:
        if i < pivot: # 9. 렙이 pivot보다 작으면 pivot에서 렙을 뺀 값을 저장해 둔다.(탑 개수만큼 반복)
            sum += (pivot - i)
        
    if sum <= k: # 10. 합산 한 값을 비교(합산값이 레벨 총 합보다 작거나 같으면)
        bottom = pivot + 1 # 11. 피벗 +1 한다음 바텀으로 재 지정
        result = max(pivot, result) # 12. 반복문 돌면서 계속 저장하고 끝났을때 최대값 출력
    elif sum > k:
        top = pivot - 1

print(result)        
        





