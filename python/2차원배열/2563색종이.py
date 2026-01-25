wh = []
idx = 0
idy = 0
for _ in range(100):
    wh.append([1] * 100)
n = int(input())
for i in range(n):
    a, b = map(int,(input().split()))
    for j in range(a, a+10):
        for k in range(b, b+10):
            wh[j][k] = 0

cnt = 0
for z in range(100):
    for x in range(100):
        if wh[z][x] == 0:
            cnt += 1
print(cnt)