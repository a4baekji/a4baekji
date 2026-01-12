cro_alp = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for ch in cro_alp:
    s = s.replace(ch, '*')
print(len(s))