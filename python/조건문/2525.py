a, b = map(int, input().split())
c = int(input())

total = int((a * 60) + b + c)

if total >= 1440:
    total -= 1440
    print(int(total / 60), int(total % 60))
else:
    print(int(total / 60), int(total % 60))
#나눗셈 기호를 쓰는 순간 float 형이 되므로 int를 달아줘야 됨
#아니면 // 를 사용하면 절로 정수형 몫을 출력