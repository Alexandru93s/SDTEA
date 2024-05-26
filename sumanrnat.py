def sumaNr(n):
    if n == 0:
        return n
    else:
        return n + sumaNr(n-1)

print(sumaNr(5))
