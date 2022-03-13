a = int(input())
result = 0
j = 1
l = list(map(int, input().split()))
l.sort()
for i in l:
        if i > j:
            result = j
            break
        j += 1
if result == 0:
    result = l[-1]+1
print(result)
