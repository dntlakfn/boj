import sys
t = int(sys.stdin.readline())
f = [sys.stdin.readline() for i in range(t)]
f = sum(map(int, f))
print(f - (t - 1))

