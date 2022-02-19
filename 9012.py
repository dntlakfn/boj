# stack
T = int(input())
for _ in range(T):
    result = ""
    stack = []
    for i in input():
        if i == ")":
            if len(stack) == 0:
                result = "NO"
                break
            stack.pop()
        else: stack.append(i) 
    if len(stack) == 0:
        if result == "NO":
            print(result)
        else: print("YES")
    else: print("NO")