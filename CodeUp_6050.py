# 두 정수를 입력받아 b의 값이 a의 값 보다 크거나 같으면 True, 같지 않으면 False 출력

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(num1 <= num2)