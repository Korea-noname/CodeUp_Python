# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력
# 입력한 숫자 -1의 상태로 0까지 출력

num = input()
num = int(num)

while num != 0:
    if num != 0:
        num -= 1
        print(num)