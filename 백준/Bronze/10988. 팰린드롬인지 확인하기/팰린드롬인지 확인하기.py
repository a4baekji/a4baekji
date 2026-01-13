s = input()
result = True
if int(len(s) / 2) == 0:
    center = int(len(s) / 2)
    for i in range(0, center + 1):
        if s[i] != s[-i-1]:
            print(0)
            result = False
            break
        elif s[i] == s[-i-1]:
            result = True
    if result == 1:
        print(1)
else:
    center = int((len(s) / 2)) + 1
    for j in range(0, center):
        if s[j] != s[-j-1]:
            result = False
            print(0)
            break
        elif s[j] == s[-j-1]:
            result = True
    if result == 1:
        print(1)