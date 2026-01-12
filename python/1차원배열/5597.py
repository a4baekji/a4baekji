a = []
for i in range(1, 31):
    a.append(i) # == a = [i for i in range(1,31)]
while True:
    try:
        n = int(input())
        a.remove(n)
    except:
        break
for values in range(len(a)):
    print(a[values])
