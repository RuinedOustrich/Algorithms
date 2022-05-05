def robot(k:int, n:int):
    A = [[0 for j in range(n+1)] for i in range(k+1)]
    if n < 0 or k < 0:
        return 0
    if n == 1 and k == 1:
        return 1
    if A[k][n] != 0:
        return A[k][n]
    A[k][n] = robot(k, n - 1) + robot(n, k - 1)
    return A[k][n]


k, n = [int(x) for x in input("Введите числа: ").split()]
a = robot(k,n)
print("Количество путей:",a)
