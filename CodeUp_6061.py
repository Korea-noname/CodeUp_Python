# 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자
# 비트단위 연산자 | (vertical bar, 버티컬 바)를 사용

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(num1 | num2)