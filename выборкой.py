import random


def selection(A):

    for j in range(len(A)):
        for i in range(j+1, len(A)):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
    return(A)

A = [random.randint(0, 100) for x in range(20)]
b = selection(A)
print(b)
