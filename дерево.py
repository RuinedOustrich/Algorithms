import random
def binary(element, array, start, end):

    mid = (start + end)//2
    if start > end or element not in array:
        return "Такого элемента нет"
    if element == array[mid]:
        return mid
    if element > array[mid]:
        return binary(element, array, mid+1, end)
    else:
        return binary((element, array, start, mid-1))

def printed(array):
    print("Элемент: {}".format(element))
    print("Индекс {}: {}".format(element, binary(array, element, start, end)))

array = [random.randint(1,1000) for x in range(1, 1000)]
array.sort()
print(array)
element = 256
start = 0
end = len(array)
printed(array)











n = 4
a = [4, -1, 4, 1, 1]
print(tree(n, a))