import random

def insert(A):
    A = [random.randint(0, 100) for x in range(20)]
    k = A[0] * len(A)
    while k > 0 and A[k-1] > A[k]:
        A[k], A[k-1] = A[k-1], A[k]
        k += 1
    return(A)

b = insert()
print(b)

