# 원형 큐 -> 스택 큐 혼합
# 큐
# 파이썬에서 deque


# [6, 7, 1, 2, 4, 5] # 원이라고 생각
# k = 3
# c = 1
# 반복 시작
# c가 k가 아니라면 맨 앞 빼서 맨 뒤에 넣어줌
# c랑 K가 같다면 앞에 제거, c = 1

from collections import deque
            
n, k = map(int, input().split())
result = []
l = [i for i in range(1, n+1)]
l = deque(l)
count = 1
while len(l) != 0:
    if count == k:
        result.append(l.popleft())
        count = 1
        
    else:
        count += 1
        l.append(l.popleft())
f = "<" + ", ".join(map(str, result)) + ">"

print(f)