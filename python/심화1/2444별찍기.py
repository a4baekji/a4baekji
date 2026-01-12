n = int(input())
for i in range(1, 2 * n, 2):
    emt = int((2 * n - i) / 2)
    print((" "  * emt) + ("*"  * i))

for j in range((2 * n) - 3, 0, -2):
    emt = int((2 * n - j) / 2)
    print((" "  * emt) + ("*"  * j))

