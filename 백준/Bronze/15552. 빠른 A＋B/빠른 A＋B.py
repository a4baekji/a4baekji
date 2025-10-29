import sys
n = int(input())
i = 0
result = [0] * n 
while i < n:
    a, b = map(int, (sys.stdin.readline().split()))
    result[i] = a + b
    i += 1
for values in result:
    print(values)
