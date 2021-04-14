# 두 정수를 입력받아 a가 b보다 작으면 True를, a가 b보다 크거나 같으면 false를 출력

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(num1 < num2)