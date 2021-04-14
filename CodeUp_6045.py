# 정수 3개를 입력받아 합과 평균을 출력

num1, num2, num3 = input().split()
sum = int(num1) + int(num2) + int(num3)
average = sum / 3
print(sum,format(average,".2f"))