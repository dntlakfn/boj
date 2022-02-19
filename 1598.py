x, y = map(int, input().split())
max_value = max(x, y)
min_value = min(x, y)
data = abs(x-y)
share, rem = divmod(data, 4)
if share == 0 :
    if rem == 0:
        print('0')
    else: print(5-rem)
elif rem == 0:
    print(share)
else:
    temp = share * 4 + min_value
    if temp < max_value:
        a = max_value % 4
        b = temp % 4
        if a == 0: print(share + rem)
        if a != 0 and b > a:
            print(1 + share + rem)
        elif a != 0 and b < a: print(share + rem)




