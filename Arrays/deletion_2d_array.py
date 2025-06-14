import numpy as np

arr_2d = np.array([[1, 2, 3], [2, 4, 6], [7, 10, 12]])

print(arr_2d)

new_2d_arr = np.delete(arr_2d, 0, axis=0) # delete row
print(new_2d_arr)

new_2d_arr = np.delete(arr_2d, 1, axis=1) # delete column
print(new_2d_arr)
