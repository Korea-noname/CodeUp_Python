# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력

text = ord(input())
check = ord('a')

while check <= text:
    print(chr(check), end = ' ')
    check += 1