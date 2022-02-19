input_num, k = map(int, input().split())
l = []
for a in range(1, input_num+1 ):
    if input_num % a == 0: 
        l.append(a)
if k > len(l):
    print(0)
else:
    l.sort()
    print(l[k-1])
