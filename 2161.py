l = []
bo = True
d = int(input())
for i in range(1, d+1):
    l.append(i)
result = []
while len(l) != 1:
    if bo:
        result.append(l.pop(0))
        bo = not bo
    else:
        l.append(l.pop(0))
        bo = not bo
result.append(l[0])
print(*result)