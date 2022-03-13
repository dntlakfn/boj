# 학생 번호
# 1, 2, 3, 4, 5
# 학생이 뽑은 번호표(index)
# 0, 1, 1, 3, 2

# ------------> 밥순서
# 4, 2, 5, 3, 1

l = []
a = int(input())
l2 = list(map(int, input().split()))
f = 1
for i in range(a):
    l.insert(l2[i], f)
    f += 1
l.reverse()
print(" ".join(list(map(str, l))))
