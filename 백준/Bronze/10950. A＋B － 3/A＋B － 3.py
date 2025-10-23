n = int(input())
i = 0
k = 0
result = [0] * n
while i < n:
    a, b = map(int,input().split())
    result[i] = a + b
    i += 1
while k < n:
    print(result[k])
    k += 1