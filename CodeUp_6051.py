# 두 정수를 입력받아 a의 값이 b의 값과 서로 다르면 True, 같으면 False 출력

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(num1 != num2)