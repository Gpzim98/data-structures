# Binary search - cuts in the middle and compare if it is bigger or smaller
# Complexity O(Log2N)


def is_element_in_array(array, element):
    if len(array) == 0 or (len(array) == 1 and array[0] != element):
        return False

    middle = len(array) // 2

    arr1 = array[0: middle]
    arr2 = array[middle: len(array)]

    if element == array[middle]:
        return True
    elif element > array[middle]:
        return is_element_in_array(arr2, element)
    else:
        return is_element_in_array(arr1, element)


a = [1, 2, 3, 4, 5, 6, 7]
a = []
print(is_element_in_array(a, 2))
