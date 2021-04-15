# 입력된 두 정수 중 큰 값을 출력
# 삼항 연산 사용할 것

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(num1 if num1 >= num2 else num2)