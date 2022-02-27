s1, s2, s3 = map(int, input().split())
l = [0 for _ in range(20 + 20 + 40 + 1)]
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            l[i+j+k] += 1
print(l.index(max(l)))


