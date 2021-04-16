# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 출력

num = int(input())
sum = 0

for i in range(num+1):
    if i % 2 == 0:
        sum += i
        i += 1
    else: i += 1

print(sum)