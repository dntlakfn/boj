# 학생 번호
# 1, 2, 3, 4, 5
# 학생이 뽑은 번호표(index)
# 0, 1, 1, 3, 2

# ------------> 밥순서
# 4, 2, 5, 3, 1

students = int(input())
l = list(map(int, input().split()))
line = []
for i in range(len(l)):
    line.insert(l[i], i+1)
print(" ".join(map(str, line[::-1])))
