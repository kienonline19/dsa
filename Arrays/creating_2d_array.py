import numpy as np


def access_elements(arr, row_index, col_idx):
    if len(arr) == 0:
        raise ValueError("Empty array!")

    if row_index >= len(arr) or row_index < -len(arr):
        raise IndexError(f"{row_index} is a invalid row index!")

    if col_idx >= len(arr[0]) or col_idx < -len(arr[0]):
        raise IndexError(f"{col_idx} is a invalid column index!")

    return arr[row_index][col_idx]


def traverse_2d_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()


def search_2d_array(arr_2d, target):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            if arr_2d[i][j] == target:
                return [i, j]

    return -1


arr_2d = np.array([
    [12, 18, 4, 15],
    [22, 16, 14, 25],
    [23, 43, 24, 35],
    [33, 53, 34, 45]
])

print(arr_2d)

# add a column at zero index (column index)
new_2d_arr = np.insert(arr_2d, 0, [[1, 2, 3, 4]], axis=1)
print(new_2d_arr)

# add a row at zero index (row index)
new_2d_arr = np.insert(arr_2d, 1, [[1, 2, 3, 4]], axis=0)
print(new_2d_arr)

new_2d_arr = np.append(arr_2d, [[1], [2], [3], [4]], axis=1)
print(new_2d_arr)

# access elements
print(access_elements(new_2d_arr, 1, 0))

# 2d array traversal
traverse_2d_arr(new_2d_arr)

# searching in 2d array
print(search_2d_array(new_2d_arr, target=55))
