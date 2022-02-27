n = int(input())
f = int(input())
n -= n % 100
while True:
    if n % f == 0:
        break
    else:
        n += 1
if n % 100 < 10:
    print("0%d" % (n % 100))
else: print(n % 100)