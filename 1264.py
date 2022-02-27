s = 0
t = ""
while True:
    t = input()
    if t == "#":
        break
    for i in t:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            s += 1
    print(s)
    s = 0