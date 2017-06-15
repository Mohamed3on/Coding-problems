def mergesort(array):
    n = len(array)
    half = round(n / 2)
    if n == 1:
        return array
    else:
        left = mergesort(array[:half])
        right = mergesort(array[half:])
    return merge(left, right)


def merge(left, right):
    array = []

    while left and right:
        if left[0] < right[0]:
            array.append(left[0])
            left.pop(0)
        else:
            array.append(right[0])
            right.pop(0)
    if left:
        array.extend(left)
    if right:
        array.extend(right)
    return array


print(mergesort([5, 2, 3, 1, 4, 6, 22, 11, 1111, 21, 0]))
