#정렬을 마친 두 배열을 병합하기
from typing import Sequence, MutableSequence

# def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
#     '''정렬을 마친 배열 a와 b를 병합하여 c에 저장'''
#     pa, pb, pc = 0,0,0 # 각 배열의 커서
#     na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소수

#     while pa < na and pb < nb:
#         if a[pa] <= b[pb]:
#             c[pc] = a[pa]
#             pa += 1
#         else:
#             c[pc] = b[pb]
#             pb += 1
#         pc += 1

#     # while pa < na:
#         c[pc] = a[pa]
#         pa += 1
#         pc += 1
    
#     while pb < nb:
#         c[pc] = b[pb]
#         pb += 1 
#         pc += 1

# if __name__ == '__main__':
#     a = [2,4,6,8,11,13]
#     b = [1,2,3,4,9,16,21]
#     c = [None] * (len(a) + len(b))
#     print('정렬을 마친 두 배열의 병합을 수행합니다. ')

#     merge_sorted_list(a,b,c) # 배열 a와 b를 병합하여 c에 저장

#     print('배열 a와 b를 병합하여 배열 c에 저장했습니다. ')
#     print(f'배열 a: {a}')
#     print(f'배열 b: {b}')
#     print(f'배열 c: {c}')

#--------------------------------------------#
def merge_sort(a: MutableSequence) -> None:
    '''병합 정렬'''
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        '''a[left] ~ a[right]를 재귀적으로 병합정렬'''
        if left < right:
            center = (left + right) // 2
            _merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right) # 배열 뒷부분을 병합 정렬

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k +=1
            
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    
    n = len(a)
    buff = [None] * n # 작업용 배열 생성
    _merge_sort(a, 0, n-1) # 배열 전체를 병합 정렬
    del buff # 작업용 배열을 소멸

if __name__ == '__main__':
    print('병합 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num) :
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)   # 배열 x를 병합정렬

    print('오름차순으로 정렬 했습니다. ')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


