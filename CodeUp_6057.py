# 2개의 정수값이 입력될 때, 그 불 값이 서로 같을 때에만 True를 출력

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(bool(num1 == num2))