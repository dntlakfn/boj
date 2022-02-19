import sys
g = sys.stdin.readline()
c = 0
for i in range(int(g)):
    t = sys.stdin.readline()
    if int(t) == 1:
        c += 1
if c > int(g)-c:
    print("Junhee is cute!")
else: print("Junhee is not cute!")
