# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력

st, nd = input().split() # 1,1 입력 가정
st, nd = int(st), int(nd)
value = 1
increase, nd_increase = 1, 1

while value != 0:
    if increase <= st: # 첫 번째 주사위
        if nd_increase <= nd:
            print(increase,nd_increase)
            nd_increase += 1
        else: 
            increase += 1
            nd_increase = 1
    else: value = 0