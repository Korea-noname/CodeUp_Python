# 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때만 True를 출력

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(bool(num1 and num2))