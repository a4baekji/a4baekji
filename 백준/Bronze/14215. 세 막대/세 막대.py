a, b, c = map(int,input().split())
if(max(a, b, c) >= a + b + c - max(a, b, c)):
    n = a + b + c - max(a, b, c) -1
    print(n + a + b + c - max(a, b, c))
else:
    print(a + b + c)