import sys
input = sys.stdin.readline

n = int(input())
stick_list = []
while n:
    stick = int(input())
    if stick_list:
        while stick_list and stick_list[-1] <= stick:
            stick_list.pop()
        stick_list.append(stick)
    else: stick_list.append(stick)
    n -= 1
print(len(stick_list))