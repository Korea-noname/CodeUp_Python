# 입력된 세 정수 중 가장 작은 값을 출력
# 삼항 연산 사용할 것

num1, num2, num3 = input().split()
num1, num2, num3 = int(num1), int(num2), int(num3)
print((num1 if num1 < num2 else num2)
if ((num1 if num1 < num2 else num2) < num3) else num3)