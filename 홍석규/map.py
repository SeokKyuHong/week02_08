str_list = ['1', '2', '3', '4', '5', '6', '7']
int_list = [1,2,3,4,5,6,7]
# 기본 형태
# map(function, iterable)

# 1. 함수를 사용한 예제(함수사용)
# test 함수와 map 함수를 이용해 리스트의 모든 요소를 1씩 더한다.
# 그밖에 모든 요소 제곱, 소수점 올림 등을 사용할 수 있다. 
def test(n):
    return n+1
result1 = list(map(test, int_list))
print(result1)
# 결과 : [2, 3, 4, 5, 6, 7, 8]

# 2. 람다(lambda)를 사용한 예제
# 이름없는 함수(lambda)를 사용하여 단순한 함수는 더 간편히 사용 할 수 있다.
result2 = list(map(lambda x: x*2, int_list))
print(result2)
# 결과 : [2, 4, 6, 8, 10, 12, 14]

# 3. 문자->정수, 정수->문자 변환, 1~N까지의 정수 리스트로 만들기
# 알고리즘에서 많이 사용되는 유형
result3 = list(map(str, int_list))
result4 = list(map(int, str_list))
result5 = list(map(int, range(1,5+1)))
print(result3)
print(result4)
print(result5)
# 결과 : ['1', '2', '3', '4', '5', '6', '7']
# 결과 : [1, 2, 3, 4, 5, 6, 7]
# 결과 : [1, 2, 3, 4, 5]

# 4. if 식을 사용한 예제
# map과 함께 if 문을 사용 하여 조건에 맞는 요소만 맵핑 할 수 있다.
result6 = list(map(lambda x : x if x<3 else x+2, int_list))
print(result6)
# 결과 : [1, 2, 5, 6, 7, 8, 9]



