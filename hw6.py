"""
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


array = [1, 3, 5, 7, 9, 11, 13]
number = 9

result = binary_search(array, number)

if result != -1:
    print("Искомый элемент найден c индексом: ", result)
else:
    print("Искомый элемент не найден")
