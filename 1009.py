T = int(input())

ar = {
    2 :[2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

for i in range(T):
    a, b = map(int, input().split())
    mod = a % 10
    if mod == 1:
        print(1)
    elif mod == 0:
        print(10)
    else:
        print(ar[mod][b % len(ar[mod])-1])