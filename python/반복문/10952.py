import sys
result = []
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==0 & b==0:
        break
    result.append(a + b)
for values in result:
    print(values)
