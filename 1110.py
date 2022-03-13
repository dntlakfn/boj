num = int(input())
d = num
result = 1
num = (num % 10) * 10 + (num % 10 + num // 10) % 10
while num != d:
    num = (num % 10) * 10 + (num % 10 + num // 10) % 10
    result += 1
print(result)
