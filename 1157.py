# 문자열에서 가장 많이 사용된 알파벳 찾기
# 대소문자 비교하지 않음 (같은 것으로 본다)
# 만약에 최대 값이 같은 알파벳이 있으면 ? 출력

# 1,000,000 크기



# a = list(input().lower())
# m = 0
# result = ''
# t = 0
# a.sort()
# while len(a) != 0:
#     t = a.count(a[0])
#     if t > m:
#         m = t
#         result = a[0].upper()
#     elif t == m:
#         result = "?"
#     a = a[t:]
# print(result)
        

# Hash테이블 -> 딕셔너리
alphaCount = {}
s = input().upper()
for c in s:
    if c not in alphaCount.keys():
        alphaCount[c] = 1
    else:
        alphaCount[c] += 1

# 1, 4, 4, 1
m = max(alphaCount.values()) # 4
result = [key for key, v in alphaCount.items() if m == v] # [i, s]
print(result[0] if len(result) == 1 else '?')
