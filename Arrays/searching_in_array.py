import array


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr_int = array.array('i', [4, 1, 2, 3, 5, 7, -10])

print(linear_search(arr_int, 30))
