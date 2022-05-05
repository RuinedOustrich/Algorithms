import random

def binary_search_recursive(array, element, start, end):
    if start > end or element not in array:
        return "Такого элемента нет"
    mid = (start + end) // 2
    if element == array[mid]:
        return mid
    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid - 1)
    else:
        return binary_search_recursive(array, element, mid + 1, end)

def printed(array):
    print("Ищем {}".format(element))
    print("Индекс {}: {}".format(element, binary_search_recursive(array, element, start, end)))





array = [random.randint(1,1000) for x in range(1, 1000)]
array.sort()
print(array)
element = 256
start = 0
end = len(array)
printed(array)

