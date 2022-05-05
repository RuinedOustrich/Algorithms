import random


def quick_sort(A):
    if len(A) <= 1:
        return
    left = []
    middle = []
    right = []
    barrier = A[0]
    for x in A:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    k = 0
    quick_sort(left)
    quick_sort(right)
    for x in left+middle+right:
        A[k] = [x]
        k += 1







random_list_of_nums = [random.randint(1, 10000) for x in range(1, 100)]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

