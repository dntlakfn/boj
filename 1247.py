import sys

for i in range(3):
    total = 0
    for i in range(int(sys.stdin.readline())):
        total += int(sys.stdin.readline())
    if total > 0:
        print("+")
    elif total < 0:
        print("-")
    else: print("0")
