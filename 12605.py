a = int(input())
for i in range(1, a+1):
    l = input().split()
    l.reverse()
    print("Case #%d: %s" % (i, " ".join(l)))