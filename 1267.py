n = int(input())
y = 0
m = 0
c = input().split()
for i in c:
    y += (int(i) // 30 + 1) * 10
    m += (int(i) // 60 + 1) * 15
if m > y:
    print('Y', y)
elif m == y:
    print('Y', 'M', y)
else: print("M", m)