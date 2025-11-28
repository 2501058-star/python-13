def x(n):
    for i in range(0, n + 1):
        if i % 2 != 0:
            print(i, end=' ')
    print() 

num = int(input("양수 입력: "))
x(num)