import sys
i = 0
k = 0
n = int(input())
result = [0] * n
while i < n:
    a, b = map(int, sys.stdin.readline().split())
    result[i] = a + b
    i += 1
while k < n:
    print("Case #%d: %d" %(k+1, result[k]))
    k += 1