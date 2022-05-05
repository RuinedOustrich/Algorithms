def stepen(a,n):
    if n == 0:
        return 1
    return stepen(a, n-1) * a

a = int(input())
n = int(input())
b = stepen(a,n)
print(b)
