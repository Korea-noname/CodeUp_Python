# 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력
# 비트단위 연산자 ^ (xor, circumflex/caret, 서컴플렉스,카릿)을 사용

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(num1 ^ num2)