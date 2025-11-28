def x(a, b, c, d):
    max_x = max(a, b, c, d)
    min_x = min(a, b, c, d)
    
    return max_x, min_x

n1, n2, n3, n4 = map(int, input("숫자 4개 입력: ").split())

maximum, minimum = x(n1, n2, n3, n4)

print(f"최댓값: {maximum}, 최솟값: {minimum}")