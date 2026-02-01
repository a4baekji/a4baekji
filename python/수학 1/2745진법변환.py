N = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16,
      "H" : 17, "I" : 18, "J" : 19, "K" : 20, "L" : 21, "M" : 22, "N" : 23, 
      "O" : 24, "P" : 25, "Q" : 26, "R" : 27, "S" : 28, "T" : 29, "U" : 30,
       "V" : 31, "W" : 32, "X" : 33, "Y" : 34, "Z" : 35}

n, b = (input().split())
b = int(b)
total = 0
length = len(n)

for i in range(length):
    ch = n[length - 1 - i] # 오른쪽부분
    if ch.isdigit():
        value = int(ch)
    else:
        value = N[ch]
    total += value * (b ** i)
print(total)
