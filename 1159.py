team = int(input())
a = []
d = 0
result = ''
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(team):
    name = input()
    a.append(name[0])
a.sort()
f = a[0]
for i in a:
    if f != i:
        if d >= 5:
            result += f
        f = i
        d = 0
    d += 1
if d >= 5:
    result += f
if len(result) < 1:
    print("PREDAJA")
else: print(result)