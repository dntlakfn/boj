import sys

input = sys.stdin.readline
for _ in range(3):
    s = 0
    t = int(input())
    for _ in range(t):
        s += int(input())
    if s < 0:
        print('-')
    elif s > 0:
        print('+')
    else: 
        print('0')
    

