s = input()
result = 0
i = 0

while i < len(s):
    if s[i:i+3] == 'dz=':
        result += 1
        i += 3
    elif s[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        result += 1
        i += 2
    else:
        result += 1
        i += 1
print(result)
