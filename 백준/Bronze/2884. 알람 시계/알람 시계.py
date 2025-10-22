h, m = map(int, input().split())

total = h * 60 + m - 45

if total < 0:
    total += 1440

print((total // 60), (total % 60))