# 3개의 정수가 입력되었을 때, 짝수만 출력

num1, num2, num3 = input().split()
num1, num2, num3 = int(num1), int(num2), int(num3)

if num1 % 2 == 0:
    print(num1)

if num2 % 2 == 0:
    print(num2)

if num3 % 2 == 0:
    print(num3)