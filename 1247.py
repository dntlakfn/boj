from msilib.schema import Error
import sys

input = sys.stdin.readline
s = 0
for _ in range(3):
    t = int(input())
    for _ in range(t):
        s += int(input())
    if s < 0:
        print('-')
        s = 0
    elif s > 0:
        print('+')
        s = 0
    else: 
        print('0')
        s = 0
