import math
result = 0
a = []

M = int(input())
N = int(input())

for i in range(M, N + 1):
    if i < 2:
        continue

    is_Prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_Prime = False
            break
    if is_Prime:
        result += i
        a.append(i)
if result == 0:
    print(-1)
else:
    print(result)
    print(min(a))
