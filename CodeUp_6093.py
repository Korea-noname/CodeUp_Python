# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

# 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부르는데,
# 영일이는 선생님이 부른 번호들을 기억하고 있다가 거꾸로 불러보는 것을 해보고 싶어졌다.

# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력

# num = int(input())
# a = list(map(int, input().split()))

# print(" ".join(repr(i) for i in reversed(a)))

num = int(input())
s_num = list(map(str, input().split()))
for i in s_num[::-1]:
  print(i, end= ' ')