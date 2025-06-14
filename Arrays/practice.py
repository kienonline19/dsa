from array import *



arr_int = array('i', [1, 2, 3, 4, 5])

for e in arr_int:
    print(e, end=' ')

print()

print(arr_int[0])
print(arr_int[3])

arr_int.append(6)

print(arr_int)

arr_int.insert(3, 11)
print(arr_int)

my_arr = array('i', [10, 11, 12])

arr_int.extend(my_arr)

print(arr_int)

arr_int.fromlist([20, 21, 22])

print(arr_int)

arr_int.remove(11)

print(arr_int)

print(arr_int.pop())
print(arr_int)

print(arr_int.index(21))

arr_int.reverse()

print(arr_int)

print(arr_int.buffer_info())

arr_int.append(11)
print(arr_int.count(110))

str_tmp = arr_int.tobytes()

print(str_tmp)

ints = array('i')
ints.frombytes(str_tmp)

print(ints)

print(ints.tolist())

# char_arr = array('u', list("abcd"))
# char_arr.append('e')

# print(char_arr)

print(arr_int)
print(arr_int[:])