c = int(input())
for i in range(c):
    arr = list(map(int, input().split()))
    n = arr[0]
    smart_count = 0
    scores = arr[1:]
    avg = sum(scores) / n
    for j in scores:
        if j > avg:
            smart_count += 1
    rate = smart_count / n * 100
    print("%.3f" % (rate) + "%")




