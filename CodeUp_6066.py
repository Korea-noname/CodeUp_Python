# 3개의 정수가 입력되었을 때, 짝/홀을 출력

num1, num2, num3 = input().split()
num1, num2, num3 = int(num1), int(num2), int(num3)

print("even" if num1 % 2 == 0 else "odd")
print("even" if num2 % 2 == 0 else "odd")
print("even" if num3 % 2 == 0 else "odd")