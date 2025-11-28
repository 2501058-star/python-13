def x(x_list):
    total = 0
    for num in x_list:
        total += num
    print(f"리스트 값의 누적 합: {total}")

a = [1, 2, 3, 4, 5]
x(a)