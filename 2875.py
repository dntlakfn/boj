# N명의 여학생
# M명의 남학생
# 조건-1 여학생 2명, 남학생 1명 한 팀
# 조건-2 K명은 인턴쉽 프로그램에 반드시 참여

# step-1 최대한 많은 팀 수 부터 찾기 3팀
# step-2 남아있는 학생 수 K 보다 크거나 같다면 3 리턴
# step-3 남아있는 학생 수가 K보다 작다면 팀 전체 수를 빼준다
# step-3-1 K가 6이면 3*2 4<=K<=6 2팀, 7<=k<=9 3팀

n, m, k = map(int, input().split())
team = 0
# step-1
while n >= 2 and m >= 1:
    team += 1
    n -= 2
    m -= 1

# 나머지 학생 수
students = n + m
# step-2
if students >= k:
    print(team)
else:
    # step-3
    # 7 3 4  team=3, students=1, k=4
    realK, mod = divmod((k - students), 3)   # 1, 0
    if realK == 0: # 한명 아니면 두명이 필요함
        print(team - 1)
    else:
        if mod != 0:
            print(team - realK - 1)
        else:
            print(team - realK)






