import random

def counting_sort(alist, largest):
    c = [0]*(largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1
    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing

    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None]*len(alist)

    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result

A = [random.randint(0, 25) for x in range(20)]
a = counting_sort(A, 25)
print(a)