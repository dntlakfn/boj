M = int(input())
d = {
    1: True,
    2: False,
    3: False
}
for i in range(M):
    x, y = map(int, input().split())
    d[x], d[y] = d[y], d[x]
for k, v in d.items():
    if v: print(k)
    