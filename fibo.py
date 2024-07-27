def fibonnaci(n):
    a, b = 0,1
    result = []

    if n == 0:
        return a
    elif n < 0:
        return a
    elif n == 1:
        return b

    while a <= n:
        result.append(a)
        a, b = b, a+b,
    return result

print(fibonnaci(-10))