a, b = input().split()
r_a = int(str(a[::-1])) #문자열 슬라이싱으로 거꾸로 읽은 후 정수형으로 변
r_b = int(str(b[::-1]))

if r_a > r_b:
    print(r_a)
else:
    print(r_b)
