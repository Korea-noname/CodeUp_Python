# 실수 2개를 입력, a를 b로 나눈 값을 출력
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력

f1, f2 = input().split()
sum = float(f1) / float(f2)
print(format(sum,".3f"))