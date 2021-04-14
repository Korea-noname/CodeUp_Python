# 정수 2개를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산
# 단 0 <= a, b <= 2147483647, b는 0이 아니다

num1, num2 = input().split()
sum = int(num1) + int(num2)
print(sum)
sum = int(num1) - int(num2)
print(sum)
sum = int(num1) * int(num2)
print(sum)
sum = int(num1) // int(num2)
print(sum)
sum = int(num1) % int(num2)
print(sum)
sum = int(num1) / int(num2)
print(format(sum,".2f"))