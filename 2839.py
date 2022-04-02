# 상근이는 N 킬로그램 설탕을 배달해야 한다.
# 봉지는 3, 5가 있다.

# 18 -> 5*3, 3*1 -> 4개 이게 답
# 18 -> 3*6 -> 6개
# 만약, 정확하게 N킬로그램을 만들 수 없다면 -1

# 그리디 알고리즘 (탐욕 알고리즘)

n = int(input())
result = 0

while n != 0:
    if n % 5 == 0:
        result += n // 5
        break

    n -= 3
    result += 1

    if n < 0:
        result = -1
        break

print(result)
