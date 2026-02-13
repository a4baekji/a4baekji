import math
while(1):
    n = int(input())
    if(n == -1):
        break
    a = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a.append(i)
            if i != n // i:
                a.append(n // i)
    a.remove(n)
    a.sort()
    result = sum(a)

    if(result == n):
        print(f"{n} = " + " + ".join(map(str, a)))
    else:
        print(f"{n} is NOT perfect.")