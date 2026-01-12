import sys
result = []
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a <= 0 or b >= 10:
            break
        result.append(a+b)
    except:
        break
for values in result:
    print(values)