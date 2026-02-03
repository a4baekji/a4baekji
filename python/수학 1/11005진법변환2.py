n, b = map(int, input().split())

result = ""

while n > 0:
    r = n % b
    if r < 10:
        result += str(r)
    else:
        result += chr(r + 55)
    n //= b

print(result[::-1])