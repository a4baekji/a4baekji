h, m = map(int, input().split())
result = 0

if h == 0:
    h = h + 1440
    result = h + m - 45
    print(int((result / 60)), int((result % 60)))
else:
    h = h * 60
    result = h + m - 45
    print(int((result / 60)), int((result % 60)))

// 코드가 간결하지 못하며 같은 식이 반복, h = 0 일때 h는 단위가 시간이기에
단위의 통일이 안되어 오류
// 그저 운 좋게 입출력이 맞아 떨어지는 코드