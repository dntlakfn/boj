while True:
    t = input()
    a = 2 + len(t)-1
    if t == '0':
        break
    for i in t:
        if i == '1':
            a += 2
        elif i == '0':
            a += 4
        else: a += 3
    print(a)