a = input()
b = input()

a_list = list(a)
b_list = list(b)
i = 1
final = 0

while b_list:
    result = 0
    result = int(a) * int(b_list.pop())
    print(result)
    final += result * i
    i *= 10

print(final)

