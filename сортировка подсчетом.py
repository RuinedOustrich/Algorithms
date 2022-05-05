import random
def insert(A):
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return(A)

A = [random.randint(1, 10) for x in range(1,10)]
Func = insert(A)
print(Func)
