a, b = map(int, input().split())
c = int(input())

total = int((a * 60) + b + c)

if total >= 1440:
    total -= 1440
    print(int(total / 60), int(total % 60))
else:
    print(int(total / 60), int(total % 60))