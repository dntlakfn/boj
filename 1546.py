# 가장 큰 점수 M
# 모든 점수를  점수/M*100 값으로 고침
# M = 70, 수학 50, 수학점수는 50/70*100이 되어 71.43

# N = 과목 수
# 두 번째 입력은 점수들 문자열

# step-1
# M = 점수 리스트 중에서 최대 점수 구하기
# step-2
# 모든 점수들 다시 구하기
# step-3
# 평균 구하기

# 3
# 40 80 60

n = int(input())
result = 0
score = list(map(int, input().split()))
# step-1
M = max(score)
for i in score:
    result += i/M*100
print(result / n)

