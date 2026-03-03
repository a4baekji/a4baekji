x, y, w, h = map(int, input().split())
r1 = w - x
r2 = h - y
print(min(x, y, r1, r2))