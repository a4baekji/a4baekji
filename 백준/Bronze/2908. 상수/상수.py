a, b = input().split()
r_a = int(str(a[::-1]))
r_b = int(str(b[::-1]))

if r_a > r_b:
    print(r_a)
else:
    print(r_b)
