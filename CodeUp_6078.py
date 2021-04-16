# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하게 작성

value = 1

while value != 0:
    text = input()
    if text != 'q':
        print(text)
        value = 1
    else: 
        print(text)
        value = 0