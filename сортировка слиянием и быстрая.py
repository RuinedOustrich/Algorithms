import random

def merge_sort(T):
    if len(T) <= 1:
        return
    middle = len(T)//2
    left = [T[i] for i in range(0,middle)]
    right = [T[i] for i in range(middle, len(T))]
    merge_sort(left)
    merge_sort(right)
    C = merge(left, right)
    for i in range(len(T)):
        T[i] = C[i]
    return T

def merge(A:list, B:list):# Сортировка слиянием
    C = [0] * (len(A)+len(B))
    i, k, n = 0, 0, 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n]=A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return(C)

A =[random.randint(1,100) for x in range(1,67)]
merge_sort(A)
print(A)
