N, m, M, T, R = map(int, input().split())
n_m = m
time = 0
if M - m < T:
    print(-1)
else:    
    while N != 0:
        if n_m + T <= M:
            n_m += T
            N -= 1
        elif n_m - R >= m:
            n_m -= R
        else:
            n_m = m
        time += 1
        
    print(time)
        