# 문자 1개 입력, 그 다음 문자 출력
# 영문자 A의 다음 문자는 B, 숫자 0의 다음 문자는 1

text = ord(input())
print(chr(text + 1))