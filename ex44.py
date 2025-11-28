def x(start, end):
    sum_x = 0
    for i in range(start, 10):
        for j in range(end, 10):
            if i * j >= 30:
                sum_x += (i * j)
    return sum_x

i, j = map(int, input("2이상 9이하 양수 2개 입력: ").split())
result = x(i, j)
print(f"곱이 30 이상인 경우의 합: {result}")