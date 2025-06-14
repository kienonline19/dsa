import array
import numpy as np

my_array = array.array('i')

print(type(my_array))
print(len(my_array))
print(my_array)

my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1)

np_array = np.array([], dtype=int)

print(np_array)

np_array1 = np.array([1, 2, 3, 4, '1'], dtype=int)

print(np_array1)
